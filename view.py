from controller import ReversiController

class BoardView:
    def __init__(self):
        self.controller=ReversiController()
        
    def print_board(self):
        size = len(self.controller.board())
        print("  " + " ".join(str(i) for i in range(size)))
        for i, row in enumerate(self.controller.board()):
            print(f"{i} " + " ".join(row))
        print(f"current turn:{self.controller.turn()}")
        print(f"you can put your stone on {self.controller.valid_moves()}")
            
    def change_stone(self):
        put_cell=input("You put your stone on:")
            #put_cellはstr型なのでtuple型へ変換
        try:
            answer = tuple(map(int, put_cell.strip("()").split(",")))
        except ValueError:
            answer = None
        if answer in self.controller.valid_moves():
            x,y=map(int, put_cell.strip("()").split(","))
            self.controller.put(x,y)
        else:
            print("please input correct answer")

    def run(self) -> None:
        while self.controller.check_end()==True:
            self.print_board()
            self.change_stone()
        print("game set")


