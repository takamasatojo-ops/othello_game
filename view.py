from model import ReversiModel

class BoardView:
    def __init__(self):
        self.model=ReversiModel()
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
    
    def print_all(self, model_board, model_turn, model_valid_moves,model_input_cell):
        self.print_board(model_board)
        if model_turn == 1:
            self.turn="B"
        elif model_turn == 2:
            self.turn="W"
        if model_input_cell==0:
            print("Please input correct answer")
        print(f"current turn:{self.turn}")
        print(f"you can put your stone on {model_valid_moves}")
    
    def print_board(self,model_board):
        for x in range(8):
            for y in range(8):
                if model_board[x][y] == 0:
                    self.board[x][y] = "･"
                elif model_board[x][y] == 1:
                    self.board[x][y] = "B"
                elif model_board[x][y] == 2:
                    self.board[x][y] ="W"
                elif model_board[x][y] == 3:
                    self.board[x][y] = "*"
        print("  " + " ".join(str(i) for i in range(8)))
        for i, row in enumerate(self.board):
            print(f"{i} " + " ".join(row))
    
    def change_stone(self):
        put_cell=input("You put your stone on:")
        return put_cell
    
    def end_game(self,model_board, model_winner, model_num_B, model_num_W):
        self.print_board(model_board)
        print("game set")
        print(f"number of Black is {model_num_B}")
        print(f"number of White is {model_num_W}")
        if model_winner==1:
            self.winner="Black"
        elif model_winner == 2:
            self.winner="White"
        elif model_winner == 3:
            self.winner="Draw"
        print(f"winner is {self.winner}")
        




