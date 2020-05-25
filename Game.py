from Deck import Shoe
from Dealer import Dealer
from Player import Player
import random
from BasicStrategyPlayer import BasicStrategyPlayer
from ProbabilityPlayer import ProbabilityPlayer

import time
class Game:
    DECKS = 1

    #Initialize
    def __init__(self, cash):
        self.shoe = Shoe(self.DECKS) #Create a shoe with 6 decks of cards

        #Initialize players
        self.dealer = Dealer(0)
        self.player = ProbabilityPlayer(cash)
        self.player.cardsLeft = self.shoe.copy()

        self.shoe.shuffle() #Shuffle shoe

        #Split Card
        if self.DECKS > 2:
            self.cutCard = random.randint(30, 60)
        else: 
            self.cutCard = 10
        self.playing = True

        #Number of hands
        self.games = 0

        #Begin Game
        self.start()

    #Start Game
    def start(self):
        #Deal new hands to players
        self.dealHand()

        #Check for naturals
        if self.dealer.hand[0].score == 21 and self.player.hand[0].score < 21:
            self.endGame()
        elif self.player.hand[0].score == 21 and self.dealer.hand[0].score < 21:
            self.player.cash += self.player.bet/2
            self.endGame()

        #If not naturals then players turn
        self.playersTurn()

    #Deals brand new hands from shoe to the players
    def dealHand(self):
        self.dealer.newHand()
        self.dealer.hand[0].addCard(self.shoe.pop())
        self.dealer.hand[0].addCard(self.shoe.pop())
        self.player.cardsLeft.pop(self.player.cardsLeft.index(self.dealer.hand[0][1]))

        self.player.newHand()
        self.player.hand[0].addCard(self.shoe.pop())
        self.player.cardsLeft.pop(self.player.cardsLeft.index(self.player.hand[0][0]))
        self.player.hand[0].addCard(self.shoe.pop())
        self.player.cardsLeft.pop(self.player.cardsLeft.index(self.player.hand[0][1]))
        
    #Players Turn
    def playersTurn(self):
        
        #For each hand that the player has
        for hand in self.player.hand:
            
            while hand.playing: #While the specific hand wants to continue
                self.preShow()
                if len(hand) == 1: #The second card after a split is left undealt
                    hand.addCard(self.shoe.pop())
                #Let the player decide given their hand and the dealers upcard
                play = self.player.turn(hand, self.dealer.hand[0][1])

                if play == "Hit":
                    hand.addCard(self.shoe.pop())
                    self.player.cardsLeft.pop(self.player.cardsLeft.index(hand[-1]))
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

        self.player.cardsLeft.pop(self.player.cardsLeft.index(self.dealer.hand[0][0]))
        if len(self.player.hand) == 1: #If the player only has one hand that busted end the game
            if self.player.hand[0].score > 21:
                self.endGame()
        self.dealersTurn() #Dealers Turn
            
    def dealersTurn(self):
        #self.postShow()

        while self.playing:
            if self.dealer.turn() == "Hit":
                self.dealer.hand[0].addCard(self.shoe.pop())
                self.player.cardsLeft.pop(self.player.cardsLeft.index(self.dealer.hand[0][-1]))
            else:
                self.endGame()
        
            
    def endGame(self):
        self.postShow()
        #self.player.cardsLeft.pop(self.player.cardsLeft.index(self.dealer.hand[0][0]))
        for hand in self.player.hand:
            hand.checkWin(self.dealer.hand[0].score)
            if hand.win == True:
                self.player.cash += hand.bet
            elif hand.tie == True:
                continue
            else: 
                self.player.cash -= hand.bet
        self.games += 1
        print(str(self.games) + "\n\n")
        if len(self.shoe) > self.cutCard:
            self.start()
        else: 
            self.playing = False

    def preShow(self):
        output = "Dealer: "
        for index,card in enumerate(self.dealer.hand[0]):
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
            output += "Score: " + str(hand.score) + " Bet: " + str(hand.bet)

        print(output)
    
    def postShow(self):
        output = "Dealer: "
        for card in self.dealer.hand[0]:
            output += card.name
            output += ", "

        output += str(self.dealer.hand[0].score) + "\nPlayer: "

        for hand in self.player.hand:
            for card in hand:
                output += card.name
                output += ", "
            output += "Score: " + str(hand.score) + " Bet: " + str(hand.bet)
        print(output)