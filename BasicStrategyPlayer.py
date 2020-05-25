from Hand import Hand
from Player import Player

class BasicStrategyPlayer(Player):

    aceDecision = [
        ["Hit", "Hit", "Hit", "Double", "Double", "Hit", "Hit", "Hit", "Hit", "Hit"], #2
        ["Hit", "Hit", "Hit", "Double", "Double", "Hit", "Hit", "Hit", "Hit", "Hit"], #3
        ["Hit", "Hit", "Double", "Double", "Double", "Hit", "Hit", "Hit", "Hit", "Hit"], #4
        ["Hit", "Hit", "Double", "Double", "Double", "Hit", "Hit", "Hit", "Hit", "Hit"], #5
        ["Hit", "Double", "Double", "Double", "Double", "Hit", "Hit", "Hit", "Hit", "Hit"], #6
        ["Double", "Double", "Double", "Double", "Double", "Stand", "Stand", "Hit", "Hit", "Hit"], #7
        ["Stand", "Stand","Stand","Stand","Double","Stand","Stand","Stand","Stand","Stand"], #8
        ["Stand", "Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand"], #9
        ["Stand", "Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand"], #10
        ["Split", "Split","Split","Split","Split","Split","Split","Split","Split","Split"] #11
    ]

    otherDecision = [
        ["Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],#4
        ["Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],#5
        ["Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],#6
        ["Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"], #7
        ["Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"], #8
        ["Hit", "Double", "Double", "Double", "Double", "Hit", "Hit", "Hit", "Hit", "Hit"],#9
        ["Double", "Double","Double", "Double","Double", "Double","Double", "Double", "Hit", "Hit"],#10
        ["Double", "Double","Double", "Double","Double", "Double","Double", "Double","Double", "Double"],#11
        ["Hit", "Hit", "Stand", "Stand", "Stand", "Hit", "Hit", "Hit", "Hit", "Hit"],#12
        ["Stand", "Stand","Stand","Stand","Stand","Hit", "Hit", "Hit", "Hit", "Hit"],#13
        ["Stand", "Stand","Stand","Stand","Stand","Hit", "Hit", "Hit", "Hit", "Hit"],#14
        ["Stand", "Stand","Stand","Stand","Stand","Hit", "Hit", "Hit", "Hit", "Hit"],#15
        ["Stand", "Stand","Stand","Stand","Stand","Hit", "Hit", "Hit", "Hit", "Hit"],#16
        ["Stand", "Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand"],#17
        ["Stand", "Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand"],#18
        ["Stand", "Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand"],#19
        ["Stand", "Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand"],#20
        ["Stand", "Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand","Stand"],#21
    ]

    splitDecision = [
        [True, True, True, True, True, True, False, False, False, False], #2
        [True, True, True, True, True, True, False, False, False, False], #3
        [False, False, False, True, True, False, False, False, False, False], #4
        [False, False, False, False, False, False, False, False, False, False], #5
        [True, True, True, True, True, False, False, False, False, False], #6
        [True, True, True, True, True, True, False, False, False, False], #7
        [True, True, True, True, True, True, True, True, True, True], #8
        [True, True, True, True, True, True, False, True, False, False], #9
        [False, False, False, False, False, False, False, False, False, False], #10
        [True, True, True, True, True, True, True, True, True, True] #11
    ]

    def turn(self, hand, upcard):
        ace = False
        sum = 0

        for card in hand:
            sum += card.value
            if card.name == "Ace":
                ace = True

        if len(hand) == 2:
            if hand[0] == hand[1]:
                if self.splitDecision[hand[0].value - 2][upcard.value - 2]:
                    return "Split"
                
            if ace:
                return self.aceDecision[sum - 13][upcard.value - 2]
        
        return self.otherDecision[sum - 4][upcard.value - 2]

