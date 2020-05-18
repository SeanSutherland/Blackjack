class Dealer:
    hand = []
    score = 0
    playing = True

    def newHand(self):
        self.score = 0
        self.hand = []
        self.playing = True

    def addCard(self, card):
        self.hand.append(card)
        self.score += card.value
        self.checkLose()

    def turn(self):
        if self.score <= 16:
            self.playing = True
            return True
        else:  
            self.playing = False
            return False

    def checkLose(self):
        if self.score > 21:
            for card in self.hand:
                if card.name == "Ace" and card.value == 11:
                    card.value = 1
                    self.playing = True
                    return True
            self.playing = False
            return False
        else:
            self.playing = True
            return True
