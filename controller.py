from model import ReversiModel

class ReversiController:
    def __init__(self):
        self.model=ReversiModel()
        
    def board(self):
        return self.model.board
    
    def valid_moves(self):
        return self.model.valid_moves
    
    def put(self,x,y):
        self.model.control_board(x,y)
        
    def turn(self):
        return self.model.turn
    
    def check_end(self):
        return self.model.check_end_game
    
    def winner(self):
        return self.model.winner