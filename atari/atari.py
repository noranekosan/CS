from sys import stdin
from typing import List


class kata:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def judge(player: kata, enemies: List[kata]):
    for i, enemy in enumerate(enemies):#x,y,width,heightの当たり判定
        if player.x <= enemy.x + enemy.width \
        and player.y <= enemy.y + enemy.height \
        and player.x + player.width >= enemy.x \
        and player.y + player.height >= enemy.y:
           print('敵機 ' + str(i + 1) + ' が当たり')
           i += 1

if __name__ == '__main__':
    player = kata(*[int(x) for x in stdin.readline().rstrip().split()])
    num = int(stdin.readline().rstrip())
    enemies = []
    for _ in range(num):
        enemies.append(kata(*[int(x) for x in stdin.readline().rstrip().split()]))
    judge(player=player, enemies=enemies)
