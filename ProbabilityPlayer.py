from Hand import Hand
from Player import Player
from Deck import *

class ProbabilityPlayer(Player):

    def turn(self, hand, upcard):
        dealerHand = Hand()
        dealerHand.addCard(upcard)
        
        chanceStand = self.probStandWin(hand.score, dealerHand, self.cardsLeft)

        chanceHit = self.probHitWin(hand, dealerHand, self.cardsLeft)
        print("Payout for STAND: $" + str(chanceStand*10))
        print("Payout for HIT: $" + str(chanceHit*10))
        if chanceStand > chanceHit:
            print("STAND")
            return "Stand"
        else:
            print("HIT")
            return "Hit"
        

    def probStandWin(self, myScore, dealerHand, shoe):
        win = 0
        count = 0
        for card in shoe:

            count += 1
            tempShoe = shoe.copy()
            tempDealerHand = dealerHand.copy()

            cards = tempShoe.pop(tempShoe.index(card))
            if cards.name == "Ace":
                cards.value = 11

            tempDealerHand.addCard(cards)

            if tempDealerHand.checkLose():
                if tempDealerHand.score < 17:
                    win += self.probStandWin(myScore, tempDealerHand, tempShoe)
                elif tempDealerHand.score < myScore:
                    win += 1
                elif tempDealerHand.score > myScore:
                    win -= 1
            else:
                win += 1
        return win/count
        

    def probHitWin(self, hand, dealerHand, shoe):
        win = 0
        count = 0
        for card in shoe:
            count += 1
            tempShoe = shoe.copy()
            tempHand = hand.copy()

            tempHand.addCard(card)
            tempShoe.pop(tempShoe.index(card))

            if card.name == "Ace":
                card.value = 11

            if tempHand.checkLose():
                win += self.probStandWin(tempHand.score, dealerHand, tempShoe)
            else: 
                win -= 1
            
        return win/count
        
        
