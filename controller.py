from model import ReversiModel

class ReversiController:
    def __init__(self):
        self.model=ReversiModel()
        
    def board(self):
        return self.model.board
    
    def valid_moves(self):
        return self.model.valid_moves
    
    def put(self,x,y):
        self.model.change_stone(x,y)
        
    def turn(self):
        return self.model.turn