from model import ReversiModel
from view import BoardView

class ReversiController:
    def __init__(self):
        self.model=ReversiModel()
        self.view=BoardView()
        
    def control_board(self,x,y):
        self.model.change_stone(x,y)
        self.model.search_putting_position()
        # print(self.model.board)
        if self.model.valid_moves == set():
            self.model.search_putting_position()
            if self.model.valid_moves == set():
                self.model.check_end_game = False
                self.model.calculate_stone()
                
    def change_stone(self):
        #put_cellはstr型なのでtuple型へ変換
        put_cell=self.view.change_stone()
        try:
            answer = tuple(map(int, put_cell.strip("()").split(",")))
        except ValueError:
            answer = None
        if answer in self.model.valid_moves:
            x,y=map(int, put_cell.strip("()").split(","))
            self.control_board(x,y)
        else:
            print("please input correct answer")
    
    def run(self) -> None:
        while self.model.check_end_game==True:
            print(self.model.board)
            self.view.print_all()
            self.change_stone()
        self.view.print_board()
        print("game set")
        print(f"number of Black is {self.model.num_B}")
        print(f"number of White is {self.model.num_W}")
        if self.model.winner==1:
            self.winner="B"
        elif self.model.winner == 2:
            self.winner="W"
        elif self.model.turn == 3:
            self.turn="Draw"
        print(f"winner is {self.winner}")
        