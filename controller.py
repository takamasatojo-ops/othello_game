from model import ReversiModel

class ReversiController:
    def __init__(self):
        self.model=ReversiModel()
        
    def control_board(self,x,y):
        self.model.change_stone(x,y)
        self.model.search_putting_position()
        if self.model.valid_moves == set():
            self.model.search_putting_position()
            if self.model.valid_moves == set():
                self.model.check_end_game = False
                self.model.calculate_stone()

        return self.model.board, self.model.turn, self.model.valid_moves, self.model.winner,self.model.num_B,self.model.num_W
    
    def put(self,x,y):
        self.control_board(x,y)
        
    def board(self):
        return self.model.board
    
    def valid_moves(self):
        return self.model.valid_moves
        
    def turn(self):
        return self.model.turn
    
    def check_end(self):
        return self.model.check_end_game
    
    def winner(self):
        return self.model.winner
    
    def num_B(self):
        return self.model.num_B
    
    def num_W(self):
        return self.model.num_W