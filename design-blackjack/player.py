from abc import abstractmethod
import enum
from deck import Hand, Card

class PlayerType(enum.Enum):
    DEALER = 0
    PLAYER = 1

class Player:
    def __init__(self, hand: Hand):
        self.hand = hand
    
    def getHand(self):
        return self.hand

    def clearHand(self):
        self.hand.clearHand()
    
    def addCard(self, card: Card):
        self.hand.addCard(card)
    
    @abstractmethod
    def makeMove(self):
        pass
 
class UserPlayer(Player):
    def __init__(self, hand: Hand, balance: int):
        super().__init__(hand)
        self._balance = balance
    
    def getBalance(self):
        return self._balance

    def placeBet(self, amount):
        if amount > self._balance:
            raise ValueError("insufficient Funds")
        self._balance -= amount
        return amount
    
    def receiveWinnings(self, amount):
        self._balance += amount
    
    def makeMove(self):
        # need to ask for bet
        if self.getHand().getScore() > 21:
            return False
        move = input("draw [y/n]: ")
        return move.lower() == 'y'

class DealerPlayer(Player):
    def __init__(self, hand):
        super().__init__(hand)
        self._targetScore = 17
        
    def updateTargetScore(self, score):
        self._targetScore = score
    
    def makeMove(self):
        if self.getHand().getScore() > 21:
            return False
        return self.getHand().getScore() < self._targetScore
            
        
