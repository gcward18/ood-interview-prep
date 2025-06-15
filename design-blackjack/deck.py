from enum import Enum
import random

class Suit(Enum):
    HEART = 'hearts'
    DIAMOND = 'diamonds'
    SPADE = 'spades'
    CLUB = 'clubs'

class Card:
    def __init__(self, suit: Suit, value: int):
        self.suit = suit
        self.value = value
    
    def print(self):
        print(self.getSuit(), self.getValue())
    
    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

class Hand:
    def __init__(self):
        self.cards: list[Card] = []
        self.score: int = 0
    
    def addCard(self, card: Card) -> None:
        self.cards.append(card)
        
        if card.getValue() == 1:
            self.score += 11 if self.score + 11 <= 21 else 1
        else:
            self.score += card.getValue()
    
    def getScore(self) -> int:
        return self.score
    
    def getCards(self):
        return self.cards
    
    def clearHand(self):
        self.score = 0
        self.cards = []
    
    def print(self):
        for card in self.cards:
            card.print()

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = [Suit.CLUB, Suit.DIAMOND, Suit.HEART, Suit.SPADE]
        self.init()
        
    def init(self):
        for suit in self.suits:
            for i in range(1, 14):
                self.cards.append(Card(suit, min(i, 10)))
    
    def shuffle(self):
        for i in range(len(self.cards)):
            j = random.randint(0, 51)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    
    def draw(self):
        return self.cards.pop()
    