import module
import random

rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def buildDeck(rank, suit):
    deck = [r + ' of ' + s for r in rank for s in suit]
    return deck
    
def shuffle(deck):
    rand = [i for i in range(0, 52)]
    random.shuffle(rand)
    tempDeck = []
    for r in rand:
        tempDeck.append(deck[r])
    return tempDeck
    
def deal(deck):
    cards = [deck[i] for i in range(0, 5)]
    return cards

def main():
    deck = buildDeck(rank, suit)
    input = module.getInt("How many times would you like to shuffle: ")
    while input > 0:
        deck = shuffle(deck)
        input -= 1
    cards = deal(deck)
    print cards
    
main()