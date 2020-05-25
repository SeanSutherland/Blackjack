from Player import Player

class Dealer(Player):

    def turn(self, hand = [], upcard = []):
        hand = self.hand[0]
        if hand.score <= 16:
            return "Hit"
        else:  
            hand.playing = False
            return "Stand"

    def isDealer(self):
        return True
