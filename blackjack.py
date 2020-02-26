import deck
import random
import pdb
# 52 cards - deck containing card
#     Card class that tracks status played or not played
#     OR just an array of 52 numbers? but then i'd have to track things like
#       values of the card, suits and something to convert back and
# Methods:
# Optional Methods:

newDeck = deck.Deck()


def game(cash):
    """Plays a game of blackjack using the cards in the deck until cards are finished"""
    # playerCash = cash  # this will need to be an input field
    random.shuffle(newDeck.cards)
    # newDeck = deck.Deck()
    hand(newDeck)
    # return newDeck


def getValue(cards):
    handVal = 0
    for card in cards:
        handVal = handVal + card.numValue
    return handVal


def hand(decks):
    playerHand = [decks.cards.pop(), decks.cards.pop()]
    dealerHand = [decks.cards.pop(), decks.cards.pop()]

    print("Your hand is {0}-{1}".format(playerHand[0].name, playerHand[1].name))
    print("The dealer is showing {0}".format(dealerHand[0].name))
    action = input("Would you like to Hit(H), Stand(S), Surrender(X), or Double Down(D)?")
    if action in "hit Hit h H":
        hit(playerHand)
    # elif action in "Surrender surrender x X":
    #    TODO return 1/2 of cash to player
    #    pass
    elif action in "Double Down D d double":
        # TODO double down action
        pass
    else:
        evalWinner(playerHand, dealerHand)
    # Hit in blackjack. takes a card from the deck and adds it to the player hand


def hit(hand):  # Takes a hand and adds a card from the deck to it, and then returns the hand
    hand.append(newDeck.cards.pop())
    return hand


def evalWinner(player, dealer):
    # TODO put in rule variations for soft 17
    dealerVal = getValue(dealer)
    print("The dealer's down card is a " + dealer[1].name + " and has a total of " + str(dealerVal))
    while dealerVal < 17:
        dealer = hit(dealer)
        dealerVal = getValue(dealer)
        print("Dealer draws a {0} and has a total of {1}".format(dealer[-1].name, dealerVal))

    playerVal = getValue(player)
    if dealerVal > 21:
        print("You win")
        return 1
    if playerVal > dealerVal:
        print("You win")
        return 1
    elif playerVal == dealerVal:
        print("It's a push")
        return 0
    else:
        print("You lose")
        return -1


def main():
    input("Welcome to a Blackjack game. Press enter to continue or Ctrl-C to quit. \n")
    # TODO take input for number of decks
    game(100)


main()
