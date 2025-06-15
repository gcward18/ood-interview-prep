from board import BoardPiece, Board
from player import Player

class Game:
    def __init__(self, grid: Board, connectN:int, targetScore: int):
        self.connectN = connectN
        self.targetScore = targetScore
        self.board = grid
        
        self.players = [
            Player("Player 1", BoardPiece.RED),
            Player("Player 2", BoardPiece.YELLOW),
        ]
        
        self.score = {}
        for player in self.players:
            self.score[player.getName()] = 0
    
    def printBoard(self):
        str = []
        board = self.board.getBoard()
        ROWS, COLS = len(board), len(board[0])
        
        for row in range(ROWS):
            row_str = []
            for col in range(COLS):
                if col == 0:
                    row_str.append('|')
                    
                match board[row][col]:
                    case BoardPiece.YELLOW:
                        row_str.append(" Y ")
                    case BoardPiece.RED:
                        row_str.append(" R ")
                    case BoardPiece.EMPTY:
                        row_str.append("   ")

                row_str.append("|")
            str.append(''.join(row_str))
        
        print('\n'.join(str))
        return '\n'.join(str)
    
    def playMove(self, player: Player) -> tuple[int,int]:
        self.printBoard()
        print(f"{player.getName()}'s turn")
        cols = self.board.getCols()
        moveColumn = int(input(f"Enter column between 0 and {cols - 1} to add a piece: "))
        moveRow = self.board.placePiece(moveColumn, player.getColor())
        return (moveRow, moveColumn)
        
    def playRound(self):
        while True:
            for player in self.players:
                row, col = self.playMove(player)
                
                pieceColor = player.getColor()
                
                if self.board.checkWin(self.connectN, row, col, pieceColor):
                    self.score[player.getName()] += 1
                    return player
    
    def playGame(self):
        maxScore = 0
        winner = None
        while maxScore < self.targetScore:
            winner = self.playRound()
            print(f"{winner.getName()} won the round")
            maxScore = max(self.score[winner.getName()], maxScore)
            self.board.init()
        print(f"{winner.getName()} won game")