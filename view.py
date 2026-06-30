class BoardView:
    def __init__(self):
        self.board = [
            ["･", "･", "･", "･", "･", "･", "･", "･"],
            ["･", "･", "･", "･", "･", "･", "･", "･"],
            ["･", "･", "･", "･", "*", "･", "･", "･"],
            ["･", "･", "･", "B", "W", "*", "･", "･"],
            ["･", "･", "*", "W", "B", "･", "･", "･"],
            ["･", "･", "･", "*", "･", "･", "･", "･"],
            ["･", "･", "･", "･", "･", "･", "･", "･"],
            ["･", "･", "･", "･", "･", "･", "･", "･"],
        ]
        self.board_before_cpu = [
            ["･", "･", "･", "･", "･", "･", "･", "･"],
            ["･", "･", "･", "･", "･", "･", "･", "･"],
            ["･", "･", "･", "･", "*", "･", "･", "･"],
            ["･", "･", "･", "B", "W", "*", "･", "･"],
            ["･", "･", "*", "W", "B", "･", "･", "･"],
            ["･", "･", "･", "*", "･", "･", "･", "･"],
            ["･", "･", "･", "･", "･", "･", "･", "･"],
            ["･", "･", "･", "･", "･", "･", "･", "･"],
        ]

    def select_cpu_human(self):
        select_partner = input("Which do you play with human or CPU?:")
        return select_partner

    def select_stone(self):
        select_stone = input("Which do you choose black or white?:")
        if select_stone == "black":
            human_stone = 1
        elif select_stone == "white":
            human_stone = 2
        else:
            human_stone = None
        return human_stone

    def print_all(self, model):
        self.print_board(model.board)
        if model.turn == 1:
            self.turn = "B"
        elif model.turn == 2:
            self.turn = "W"
        print(f"current turn:{self.turn}")
        print(f"you can put your stone on {model.valid_moves}")
        if model.check_input == 0:
            self.print_correct_answer()
        if model.turn_pass == 1:
            print("Black is pass")
        elif model.turn_pass == 2:
            print("White is pass")
        else:
            pass

    def print_correct_answer(self):
        print("Please input correct answer")

    def print_board(self, model_board):
        for x in range(8):
            for y in range(8):
                if model_board[x][y] == 0:
                    self.board[x][y] = "･"
                elif model_board[x][y] == 1:
                    self.board[x][y] = "B"
                elif model_board[x][y] == 2:
                    self.board[x][y] = "W"
                elif model_board[x][y] == 3:
                    self.board[x][y] = "*"
        print("  " + " ".join(str(i) for i in range(8)))
        for i, row in enumerate(self.board):
            print(f"{i} " + " ".join(row))

    def print_cpu_select(self, model_cpu, human_stone):
        if model_cpu.cpu_put_stone is True:
            print(f"CPU selected {model_cpu.best_cpu_position}")
        else:
            pass

    def change_stone(self):
        put_cell = input("You put your stone on:")
        return put_cell

    def change_stone_cpu(self, model_cpu, human_stone):
        if model_cpu.turn == human_stone:
            put_cell_cpu = self.change_stone()
        else:
            put_cell_cpu = input("CPU put its stone(Enter)")
        return put_cell_cpu

    def end_game(self, model):
        self.print_board(model.board)
        print("game set")
        print(f"number of Black is {model.num_B}")
        print(f"number of White is {model.num_W}")
        if model.winner == 1:
            self.winner = "Black"
        elif model.winner == 2:
            self.winner = "White"
        elif model.winner == 3:
            self.winner = "Draw"
        print(f"winner is {self.winner}")
