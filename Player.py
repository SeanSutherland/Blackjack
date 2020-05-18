class Player:
    hand = []
    score = 0
    cash = 0
    playing = True

    def __init__(self, startingCash):
        self.cash = startingCash

    def newHand(self):
        self.score = 0
        self.hand = []
        self.playing = True

    def addCard(self, card):
        self.hand.append(card)
        self.score += card.getValue(self.score)
        return self.checkLose()

    def turn(self):
        play = input()
        return play

    def checkLose(self):
        if self.score > 21:
            for card in self.hand:
                if card.name == "Ace" and card.value == 11:
                    card.value = 1
                    self.score -= 10
                    self.playing = True
                    return True
            self.playing = False
            return False
        else:
            self.playing = True
            return True
