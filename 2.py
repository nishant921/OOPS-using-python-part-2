#Q-2:` Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

# * The `Deck` class should have a deal method to deal a single card from the deck
# * After a card is dealt, it is removed from the deck.
# * There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# * The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

# `Deck` Class
# * It is class of all possible cards in a deck. Total 52 cards.
# * Methods - `deal()` it will take out one card from the deck of cards.
# * Deck of cards should get shuffeled while creating the deck object.
# * `no of cards remaining in deck - <number>` should dsiplay on printing any deck object.

# `Card` class
# * It is a class of card
# * Atrributes - `suit` and `value`
# * `<suit> of <value>` should dsiplay on printing any card object.

# #Code Here

import random

class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value

    def __repr__(self):
        return "{}/{}".format(self.suit,self.value)

class Deck:
    def __init__(self):
        suits = ['Hearts','Diamonds','Clubs','Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','K','Q']
        self.cards = [Card(suit,value) for suit in suits for value in values]

    def __str__(self):
        return "Cards left " + str(len(self.cards))

    def shuffle(self):
        if len(self.cards)<52:
            print("Only full Deck can be Shuffled!")
        else:
            random.shuffle(self.cards)
        return self.cards
    
    def deal(self):
        if len(self.cards)==0:
            print("All Cards have been Dealt!")
        return self.cards.pop()

deck = Deck()
deck.shuffle()
print(deck.deal())
print(deck.deal())
print(deck)