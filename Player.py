from Hand import Hand

class Player:

    def __init__(self, startingCash):
        self.cash = startingCash
        self.hand = []
        self.bet = 0
        self.playing = False
        self.cardsLeft = []

    def newHand(self):
        self.bet = 10
        self.playing = True
        self.hand = [Hand(self.bet)]

    def addCard(self, card, index):
        if not (self.isDealer() and len(self.hand[0]) == 0):
            self.cardsLeft.pop(self.cardsLeft.index(card))
        self.hand[index].addCard(card)

    def split(self, hand):
        self.hand.append(Hand(self.bet))
        index = self.hand.index(hand)
        self.hand[-1].addCard(self.hand[index].pop())

    def turn(self, hand, upcard):
        pass

    def isDealer(self):
        return False

