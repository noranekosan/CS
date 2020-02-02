def Main():
    cards = Input()
    sootCnt, cardCnt = Count(cards)
    handNum = Judge(sootCnt, cardCnt)
    Output(cards, handNum ,cardCnt,sootCnt)

def Input():
    cards = []
    for i in range(0, 5):
        cards.append(list(map(int, input().split())))
    return cards

def Count(cards):
    sootCnt = [0 for i in range(4)]
    cardCnt = [0 for i in range(13)]
    for soot, num in cards:
        sootCnt[soot] = sootCnt[soot] + 1
        cardCnt[num - 1] = cardCnt[num - 1] + 1
    return sootCnt, cardCnt

def Judge(sootCnt, cardCnt):
    candidate = [2,3,5,6,7,8,9]
    hand = [i for i, v in enumerate(cardCnt) if v == max(cardCnt)]
    hand.sort()
    if 5 in sootCnt:
        candidate = [0, 1, 4]

    if 4  in cardCnt or 5 in cardCnt:
        return int(list(set(candidate) & set([2, 4]))[0])
    if 2  in cardCnt and 3 in cardCnt:
        return 3
    if 3 in cardCnt:
        return int(list(set(candidate) & set([4, 6]))[0])
    if cardCnt.count(2) == 2:
        return int(list(set(candidate) & set([4, 7]))[0])
    if cardCnt.count(2) == 1:
        return int(list(set(candidate) & set([4, 8]))[0])
    i = cardCnt.index(1)
    if cardCnt[i:i + 5].count(1) == 5 or cardCnt[i:i + 5].count(1) == 1:
        if hand == [0,9,10,11,12] and max(sootCnt) == 5:
            return 0
        return int(list(set(candidate) & set([1, 4, 5]))[0])

    return int(list(set(candidate) & set([4, 9]))[0])

def Output(cards, num ,cardCnt,sootCnt):
    hands = ['ロイヤルフラッシュ', 'ストレートフラッシュ', 'フォーカード', 'フルハウス',
         'フラッシュ', 'ストレート', 'スリーカード', 'ツーペア', 'ワンペア', 'ハイカード']
    soot = ['♣', '♦', '♥', '♠']
    mark = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', ]
    sentence = ''
    for card in cards:
        sentence = sentence + soot[card[0]] + mark[card[1] - 1] + ' '
    print(sentence)
    max1 = (max([i for i, v in enumerate(cardCnt) if v == max(cardCnt)]))

    min1 = (min([i for i, v in enumerate(cardCnt) if v == max(cardCnt)]))
    if hands[num] == 'ストレートフラッシュ' or hands[num] == 'フォーカード' or hands[num] == 'フルハウス' or hands[num] == 'フラッシュ' or hands[num] == 'ストレート' or hands[num] == 'スリーカード' or hands[num] == 'ツーペア' or hands[num] == 'ワンペア' or hands[num] == 'ハイカード':
        if min1 == 0:
            print(str(mark[min1]) + "の" + str(hands[num]))
        else:
            print(str(mark[max1]) + "の" + str(hands[num]))
    else:
        print(hands[num])

if __name__ == '__main__':
    Main()
