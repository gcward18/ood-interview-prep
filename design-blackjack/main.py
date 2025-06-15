from game import GameRound
from player import DealerPlayer, UserPlayer
from deck import Hand, Deck

player = UserPlayer(Hand(), 1000)
dealer = DealerPlayer(Hand())

while player.getBalance() > 0:
    round = GameRound(player, dealer, Deck()).play()