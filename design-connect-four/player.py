from board import BoardPiece

class Player:
    def __init__(self, name: str, color: BoardPiece):
        self.name = name
        self.color = color
    
    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color