from Deck import Card

class Hand(list):
    score = 0
    bet = 0
    playing = True
    win = False
    tie = False

    def __init__(self, bet = 0):
        super(Card)
        self.score = 0
        self.bet = bet
        self.playing = True
        
    def addCard(self, card):
        super().append(card)
        self.score += card.value

    def double(self):
        self.bet *= 2

    def updateScore(self):
        value = 0
        for card in self:
            value += card.value
        self.score = value

    def checkWin(self, dealersScore):
        if self.score > 21:
            self.win = False
        elif dealersScore > 21:
            self.win = True
        elif self.score > dealersScore:
            self.win = True
        elif self.score == dealersScore:
            self.win = False
            self.tie = True
        else: 
            self.win = False

    def checkLose(self):
        if self.score > 21:
            for card in self:
                if card.name == "Ace" and card.value == 11:
                    #print("Converted")
                    card.value = 1
                    self.score -= 10
                    self.playing = True
                    return True
            self.playing = False
            return False
        else:
            self.playing = True
            return True

    def copy(self):
        returner = Hand()
        for card in self:
            returner.addCard(card)
        return returner
