from Hand import Hand

class Player:
    hand = []
    cash = 0
    bet = 0
    playing = True

    def __init__(self, startingCash):
        self.cash = startingCash

    def newHand(self):
        self.bet = int(input())
        self.hand = [Hand(self.bet)]

    def split(self, hand):
        self.hand.append(Hand(self.bet))
        index = self.hand.index(hand)
        self.hand[-1].addCard(self.hand[index].pop())

    def turn(self, upcard):
        play = input()
        return play
