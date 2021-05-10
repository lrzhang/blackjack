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
# TODO 2/26 Handle aces


def game(cash):
    """Plays a game of blackjack using the cards in the deck until cards are finished"""
    # playerCash = cash  # this will need to be an input field
    random.shuffle(newDeck.cards)
    # newDeck = deck.Deck()
    finCount = 0
    handCount = 0

    while len(newDeck.cards) > 12:
        playerHand = [newDeck.cards.pop(), newDeck.cards.pop()]
        dealerHand = [newDeck.cards.pop(), newDeck.cards.pop()]
        result = hand(newDeck, playerHand, dealerHand)
        finCount += result
        handCount += 1
    print("You played {1} hands and your score is {0}".format(finCount, handCount))
    # return newDeck


def getValue(cards):
    handVal = 0
    for card in cards:
        handVal = handVal + card.numValue
    return handVal


def split(decks, playerHand, dealerHand):
    playerHand1 = [playerHand[0], decks.cards.pop()]
    playerHand2 = [playerHand[1], decks.cards.pop()]
    result = 0
    print("You split your hand. First split:")
    result += hand(decks, playerHand1, dealerHand)
    print("Now for the second split:")
    result += hand(decks, playerHand2, dealerHand)

    return result


def hand(decks, playerHand, dealerHand):
    print("------Starting New Hand------")
    print("Your hand is {0}-{1}".format(playerHand[0].name, playerHand[1].name))
    print("The dealer is showing {0}".format(dealerHand[0].name))

    # Check for Blackjack
    if any(card.numValue == 0 for card in playerHand) and any(card.numValue == 10 for card in playerHand):
        print("Congrats on blackjack")
        return 1.5

    if playerHand[0].numValue == playerHand[1].numValue:
        action = input(
            "Would you like to Hit(H), Stand(S), Split(P), Surrender(X), or Double Down(D)?")
    else:
        action = input("Would you like to Hit(H), Stand(S), Surrender(X), or Double Down(D)?")

    while action != "S":
        if action == "H":
            hit(playerHand)
            playerVal = getValue(playerHand)
            print("A {0} is dealt and your new total is {1}".format(
                playerHand[-1].name, playerVal))
            if playerVal > 21:
                break  # go to evaluating the winner
            action = input("Would you like to Hit(H), Stand(S)?")
        # elif action in "Surrender surrender x X":
            # TODO return 1/2 of cash to player
            #
        elif action == "D":
            # TODO double down action
            print("Doubling down....")
            hit(playerHand)
            return 2*evalWinner(playerHand, dealerHand)
        elif action == "P" and playerHand[0].numValue == playerHand[1].numValue:
            return split(decks, playerHand, dealerHand)
        else:
            print("That is not a valid action. Please enter a letter that corresponds to an action")
            action = input("Would you like to Hit(H), Stand(S), Surrender(X), or Double Down(D)?")

    result = evalWinner(playerHand, dealerHand)
    # Hit in blackjack. takes a card from the deck and adds it to the player hand
    return result


def hit(hand):  # Takes a hand and adds a card from the deck to it, and then returns the hand
    hand.append(newDeck.cards.pop())
    # print("New card is dealt and the new total is " + str(getValue(hand)))
    return hand


def evalWinner(player, dealer):
    # TODO put in rule variations for soft 17

    playerVal = getValue(player)
    if playerVal > 21:
        print("You lose via busting. \n \n")
        return -1

    dealerVal = getValue(dealer)
    print("The dealer's down card is a " + dealer[1].name + " and has a total of " + str(dealerVal))
    while dealerVal < 17:
        dealer = hit(dealer)
        dealerVal = getValue(dealer)
        print("Dealer draws a {0} and has a total of {1}".format(dealer[-1].name, dealerVal))

    if dealerVal > 21:
        print("Dealer busts. You win. \n \n")
        return 1
    if playerVal > dealerVal:
        print("You win. \n \n")
        return 1
    elif playerVal == dealerVal:
        print("It's a push. \n \n")
        return 0
    else:
        print("You lose. \n \n")
        return -1


def main():
    input("Welcome to a Blackjack game. Press enter to continue or Ctrl-C to quit. \n")
    # TODO take input for number of decks
    game(100)


main()
