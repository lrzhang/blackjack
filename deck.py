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
        self.name = self.nameDesc()
        self.numValue = min(value % 13, 9)  # be wary of 0 meaning ace
        # TODO may want to add in an abbreviation var
        # temp = self.name.split(' ').remove("of")
        # self.abbrev = str(temp[0][0] + temp[1][0])

        # no longer using self.value as we only care about name and numValue
        del self.value

    def suitConv(self, x):
        """Takes in integer value of the card and returns the suit"""
        x = int(x / 13)
        if(x < 4):
            suit = ["clubs", "diamonds", "hearts", "spades"]
            return suit[x]
        else:
            pass

    def nameDesc(self):
        """Returns a String describing the card"""
        faceCard = ["Jack", "Queen", "King"]
        num = self.value % 13
        nameHolder = ""
        if(0 < num < 10):
            nameHolder = str(num + 1) + " of " + self.suit
        elif(num == 0):  # 0 is an ace
            nameHolder = "Ace of " + self.suit
        elif(num >= 10):
            nameHolder = faceCard[num % 10] + " of " + self.suit
        return nameHolder


def test():
    myDeck = Deck()
    for card in myDeck.cards:
        print(card.name)


test()
