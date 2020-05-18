import random

class Shoe(list):

    def __init__(self, decks):
        for i in range(decks):
            super().extend(Deck())

    def shuffle(self):
        random.shuffle(self)



class Deck(list):
    _SINGLESUIT = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def __init__(self):
        for i in range(4):
            for name in self._SINGLESUIT:
                super().append(Card(name))


class Card():
    name = None
    value = None
    symbol = None

    def __init__(self, name):
        self.name = name
        self.setValue()
        self.setSymbol()

    def setSymbol(self):
        if self.name == "Ace" or self.name == "Jack" or self.name == "Queen" or self.name == "King":
            self.symbol = str(self.name[0])
        else: 
            self.symbol = str(self.value)

    def setValue(self):
        values = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

        if self.name == "Ten" or self.name == "Jack" or self.name == "Queen" or self.name == "King":
            self.value = int(10)
        elif self.name == "Ace":
            self.value == None
        else:
            self.value = int(values.index(self.name) + 2)
        
    def getValue(self, score):
        if self.name == "Ace":
            if score <= 10: 
                self.value = 11
            else:
                self.value = 1
        return self.value

    


