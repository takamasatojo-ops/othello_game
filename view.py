class BoardView:
    def __init__(self):
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
        self.board_before_cpu = [
        ["･","･","･","･","･","･","･","･"],
        ["･","･","･","･","･","･","･","･"],
        ["･","･","･","･","*","･","･","･"],
        ["･","･","･","B","W","*","･","･"],
        ["･","･","*","W","B","･","･","･"],
        ["･","･","･","*","･","･","･","･"],
        ["･","･","･","･","･","･","･","･"],
        ["･","･","･","･","･","･","･","･"]
        ]
    
    def select_cpu_human(self):
        select_partner=input("Which do you play with human or CPU?:")
        return select_partner
    
    def select_stone(self):
        human_stone=input("Which do you choose black or white?:")
        return human_stone
    
    def print_all(self, model_board, model_turn, model_valid_moves,model_check_input):
        self.print_board(model_board)
        if model_turn == 1:
            self.turn="B"
        elif model_turn == 2:
            self.turn="W"
        if model_check_input==0:
            self.print_correct_answer()
        print(f"current turn:{self.turn}")
        print(f"you can put your stone on {model_valid_moves}")
        
    def print_correct_answer(self):
        print("Please input correct answer")
        
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
        
    def print_all_cpu(self, model_cpu_board, model_cpu_turn, model_cpu_valid_moves,model_cpu_check_input):
        self.print_board(model_cpu_board)
        if model_cpu_turn == 1:
            self.turn="B"
        elif model_cpu_turn == 2:
            self.turn="W"
        if model_cpu_check_input==0:
            print("Please input correct answer")
        print(f"current turn:{self.turn}")
        print(f"CPU can put its stone on {model_cpu_valid_moves}")
        
    def print_cpu_select(self,cpu_select_position):
        print(f"CPU putted stone on {cpu_select_position}")
    
    def change_stone(self):
        put_cell=input("You put your stone on:")
        return put_cell
    
    def cpu_put_stone(self):
        put_cell=input("CPU put its stone(Enter)")
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
        




