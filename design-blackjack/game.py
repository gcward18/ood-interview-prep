from player import DealerPlayer, UserPlayer
from deck import Deck, Card

class GameRound:
    def __init__(self, player: UserPlayer, dealer: DealerPlayer, deck: Deck):
        self.deck = deck
        self.dealer = dealer
        self.player = player
    
    def getUserBet(self):
        bet = int(input(f"Enter User bet upto {self.player.getBalance()}: "))
        return bet
    
    def dealInitialCards(self):
        for i in range(2):
            self.dealer.addCard(self.deck.draw())
            self.player.addCard(self.deck.draw())
        print('Player Hand: ')
        self.player.getHand().print()
        dealerCard = self.dealer.getHand().getCards()[0]
        print(f"Dealer's first card: ")
        dealerCard.print()
        
    def cleanupRound(self):
        self.player.clearHand()
        self.dealer.clearHand()
        print(f"Player Balance: {self.player.getBalance()}")

    def play(self):
        self.deck.shuffle()
        
        if self.player.getBalance() <= 0:
            print("Player has no more money")
            return
        
        userBet = self.getUserBet()
        self.player.placeBet(userBet)

        self.dealInitialCards()

        # user makes moves:
        while self.player.makeMove():
            drawnCard = self.deck.draw()
            print(f"Player draws {drawnCard.getSuit()} {drawnCard.getValue()}")
            self.player.addCard(drawnCard)
            print(f"Player score: {self.player.getHand().getScore()}")
        
        if self.player.getHand().getScore() > 21:
            print("Player busts")
            self.cleanupRound()
            return

        while self.dealer.makeMove():
            card: Card = self.deck.draw()
            self.dealer.addCard(self.deck.draw())
            print("dealer drew: ")
            card.print()
        
        dealerScore = self.dealer.getHand().getScore()
        playerScore = self.player.getHand().getScore()
        print(f"Dealer {dealerScore}, Player: {playerScore} ")
        if dealerScore > 21 or playerScore > dealerScore:
            print("Player wins")
            self.player.receiveWinnings(userBet * 2)
        elif dealerScore > playerScore:
            print("Dealer wins")
        else:
            print("Round ends in a draw")
            self.play.receiveWinnings(userBet)
        self.cleanupRound()