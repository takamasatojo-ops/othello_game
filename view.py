from model import ReversiModel

class BoardView:
    def __init__(self):
        self.model = ReversiModel()
        self.board = [
        ["･","･","･","･","･","･","･","･"],
        ["･","･","･","･","･","･","･","･"],
        ["･","･","･","･","*","･","･","･"],
        ["･","･","･","B","W","*","･","･"],
        ["･","･","*","W","B","･","･","･"],
        ["･","･","･","*","･","･","･","･"],
        ["･","･","･","･","･","･","･","･"],
        ["･","･","･","･","･","･","･","･"]
        ]
    
    def print_all(self):
        print(self.model.board)
        self.print_board()
        if self.model.turn == 1:
            self.turn="B"
        elif self.model.turn == 2:
            self.turn="W"
        print(f"current turn:{self.turn}")
        print(f"you can put your stone on {self.model.valid_moves}")
    
    def print_board(self):
        for x in range(8):
            for y in range(8):
                if self.model.board[x][y] == 0:
                    self.board[x][y] = "･"
                elif self.model.board[x][y] == 1:
                    self.board[x][y] = "B"
                elif self.model.board[x][y] == 2:
                    self.board[x][y] ="W"
                elif self.model.board[x][y] == 3:
                    self.board[x][y] = "*"
        print("  " + " ".join(str(i) for i in range(8)))
        for i, row in enumerate(self.board):
            print(f"{i} " + " ".join(row))
    
    def change_stone(self):
        put_cell=input("You put your stone on:")
        return put_cell




