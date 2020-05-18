from Deck import Shoe
from Dealer import Dealer
from Player import Player
from BasicStrategyPlayer import BasicStrategyPlayer

import time
class Game:
    DECKS = 8
    shoe = []
    dealer = None
    player = None

    def __init__(self, cash):
        self.shoe = Shoe(self.DECKS)
        self.shoe.shuffle()

        self.dealer = Dealer()
        self.player = BasicStrategyPlayer(cash)

        self.start()

    def dealHand(self):
        self.dealer.newHand()
        self.dealer.addCard(self.shoe.pop())
        self.dealer.addCard(self.shoe.pop())

        self.player.newHand()
        self.player.hand[0].addCard(self.shoe.pop())
        self.player.hand[0].addCard(self.shoe.pop())

    def start(self):
        self.dealHand()
        if self.dealer.score == 21 and  self.player.hand[0].score < 21:
            self.endGame()
        elif self.player.hand[0].score == 21 and self.dealer.score < 21:
            self.player.cash += self.player.bet/2
        self.playersTurn()
        
    def playersTurn(self):
        
        for hand in self.player.hand:
            while hand.playing: 
                if len(hand) == 1:
                    hand.addCard(self.shoe.pop())

                self.preShow()
                play = self.player.turn(hand, self.dealer.hand[1])

                if play == "Hit":
                    hand.addCard(self.shoe.pop())
                elif play == "Stand":
                    hand.playing = False
                elif play == "Split":
                    self.player.split(hand)
                    hand.addCard(self.shoe.pop())
                    hand.updateScore()
                elif play == "Double":
                    hand.addCard(self.shoe.pop())
                    hand.double()

                if hand.playing:
                    hand.playing = hand.checkLose()

        if len(self.player.hand) == 1:
            if self.player.hand[0].score > 21:
                self.endGame()

        self.dealersTurn()
            
    def dealersTurn(self):
        self.postShow()

        while self.dealer.playing:
            if self.dealer.turn():
                print("Dealer Hits")
                self.dealer.addCard(self.shoe.pop())
                self.postShow()
            else:
                print("Dealer Stands")
                self.endGame()
        self.endGame()
            

            
            
    def endGame(self):
        self.postShow()
        for hand in self.player.hand:
            hand.checkWin(self.dealer.score)
            if hand.win == True:
                self.player.cash += hand.bet
            elif hand.tie == True:
                continue
            else: 
                self.player.cash -= hand.bet
        print("Your Cash: " + str(self.player.cash) + "\n\n")
        if len(self.shoe) > 30:
            self.start()

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

        for hand in self.player.hand:
            for card in hand:
                output += card.name
                output += ", "
            output += "Score: " + str(hand.score) + " Bet: " + str(hand.bet) + "\n"

        print(output)
    
    def postShow(self):
        output = "Dealer: "
        for card in self.dealer.hand:
            output += card.name
            output += ", "

        output += str(self.dealer.score) + "\nPlayer: "

        for hand in self.player.hand:
            for card in hand:
                output += card.name
                output += ", "
            output += "Score: " + str(hand.score) + " Bet: " + str(hand.bet)
        print(output)