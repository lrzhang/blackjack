import pdb

# deck of cards


class Deck():

    # cards will be from 0 to 51 inclusive. Suit order will be clubs, diamond,
    # hearts, spades
    def __init__(self):  # maybe add in number of decks?
        # create a list of cards in a card deck
        self.cards = [Card(x) for x in range(52)]


class Card():

    def __init__(self, value):
        self.suit = self.suitConv(value)
        self.value = value
        self.numValue = min(value % 13, 9)  # be wary of 0 meaning ace
        self.name = self.nameDesc()

    def suitConv(self, x):
        """Takes in integer value of the card and returns the suit"""
        x = x / 13
        if(x < 4):
            suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
            return suit[x]
        else:
            pass

    def nameDesc(self):
        """Returns a String describing the card"""
        faceCard = ["Jack", "Queen", "King"]
        nameHolder = ""
        if(0 < self.numValue < 10):
            nameHolder = str(self.numValue + 1) + " of " + self.suit
        elif(self.numValue == 0):  # 0 is an ace
            nameHolder = "Ace of " + self.suit
        elif(self.numValue >= 10):
            nameHolder = faceCard[self.numValue % 10] + " of " + self.suit
        return nameHolder


def test():
    myDeck = Deck()
