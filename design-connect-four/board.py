import enum

class BoardPiece(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2
    
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.init()
    
    def init(self):
        self.grid = [[BoardPiece.EMPTY] * self.cols for _ in range(self.rows)]
    
    def getCols(self) -> int:
        return self.cols

    def getBoard(self) -> list[list[BoardPiece]]:
        return self.grid
    
    def placePiece(self, col: int, piece: BoardPiece) -> int:
        if piece == BoardPiece.EMPTY:
            raise ValueError("Invalid Piece")
        if 0 <= col < self.cols:
            for row in range(self.rows-1, -1, -1):
                if self.grid[row][col] == BoardPiece.EMPTY:
                    self.grid[row][col] = piece
                    return row
        else:
            raise ValueError("Out of bounds")
        return 0
    
    def checkWin(self, connectN: int, row: int, col: int, piece: BoardPiece) -> bool:
        count = 0
        # check col for win
        for i in range(self.cols):
            if self.grid[row][i] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True
        
        count = 0
        # check row for win
        for i in range(self.rows):
            if self.grid[i][col] == piece:
                count += 1
            else:
                count = 0
            if count == connectN: 
                return True
        
        count = 0
        # check diagonal for win
        for r in range(self.rows):
            c = row + col - r
            if c >= 0 and c < self.cols and self.grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True
        
        count = 0
        # check anti-diagonal for win
        for r in range(self.rows-1, -1, -1):
            c = row - col + r
            if c >= 0 and c < self.cols and self.grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True
        
        return False