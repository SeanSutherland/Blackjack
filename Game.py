from Deck import Shoe
from Dealer import Dealer
from Player import Player
import time
class Game:
    DECKS = 8
    shoe = []
    dealer = None
    player = None

    def __init__(self):
        self.shoe = Shoe(self.DECKS)
        self.shoe.shuffle()

        self.dealer = Dealer()
        self.player = Player(500)

        self.deal()

    def dealHand(self):
        self.dealer.newHand()
        self.dealer.addCard(self.shoe.pop())
        self.dealer.addCard(self.shoe.pop())

        self.player.newHand()
        self.player.addCard(self.shoe.pop())
        self.player.addCard(self.shoe.pop())

    def deal(self):
        self.dealHand()
        self.preShow()

        self.playersTurn()
        
    def playersTurn(self):
        play = self.player.turn()
        if play == "Hit":
            if not self.player.addCard(self.shoe.pop()):
                self.preShow()
                print("Loser")
                self.endGame()
            else:
                self.preShow()
                self.playersTurn()
        elif play == "Stand":
            self.postShow()
            self.dealersTurn()
            
    def dealersTurn(self):
        play = self.dealer.turn()
        print(play)
        if play == "Hit":
            if not self.dealer.addCard(self.shoe.pop()):
                self.postShow()
                self.endGame()
            else:
                self.postShow()
                self.dealersTurn()
        elif play == "Stand":
            self.endGame()
            
            
    def endGame(self):
        print("Done\n\n\n\n")
        time.sleep(5)
        self.deal()

    def preShow(self):
        output = "Dealer: "
        for index,card in enumerate(self.dealer.hand):
            if index == 0: 
                output += "Hidden"
                output += ", "
                continue
            output += card.name
            output += ", "

        output += "\nPlayer: "

        for card in self.player.hand:
            output += card.name
            output += ", "
        output += str(self.player.score)
        print(output)
    
    def postShow(self):
        output = "Dealer: "
        for card in self.dealer.hand:
            output += card.name
            output += ", "

        output += str(self.dealer.score) + "\nPlayer: "

        for card in self.player.hand:
            output += card.name
            output += ", "
        output += str(self.player.score)
        print(output)