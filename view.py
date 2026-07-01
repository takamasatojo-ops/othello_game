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
        select_partner = input("人間対人間は「1」を入力、人間対CPUは「2」を入力してください:")
        return select_partner

    def select_stone(self):
        select_stone = input("あなたが黒を選ぶ場合は「1」、白を選ぶ場合は「2」を入力してください:")
        if select_stone == "1":
            human_stone = 1
        elif select_stone == "2":
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
        print(f"現在のターン:{self.turn}")
        print(f"あなたは次の場所に石を置くことができます(行,列)： {model.valid_moves}")
        if model.check_input == 0:
            self.print_correct_answer()
        if model.turn_pass == 1:
            print("黒がパスです")
        elif model.turn_pass == 2:
            print("白がパスです")
        else:
            pass

    def print_correct_answer(self):
        print("正しい値を入力してください")

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
        print("     -------列------")
        print("     " + " ".join(str(i) for i in range(8)))
        for i, row in enumerate(self.board):
            if i == 3:
                print(f"行 {i} " + " ".join(row))
            else:
                print(f" | {i} " + " ".join(row))

    def print_cpu_select(self, model_cpu):
        if model_cpu.cpu_put_stone is True:
            print(f"CPUは次を選びました：{model_cpu.best_cpu_position}")
        else:
            pass

    def change_stone(self):
        input_row = input("行番号を入力してください:")
        input_column = input("列番号を入力してください:")
        return input_row, input_column

    def change_stone_cpu(self, model_cpu, human_stone):
        if model_cpu.turn == human_stone:
            put_cell_cpu = self.change_stone()
        else:
            put_cell_cpu = input("CPUの番です(Enterを押下)")
        return put_cell_cpu

    def end_game(self, model):
        self.print_board(model.board)
        print("ゲーム終了です")
        print(f"黒石の数は {model.num_B}")
        print(f"白石の数は {model.num_W}")
        if model.winner == 1:
            self.winner = "黒が勝ちました"
        elif model.winner == 2:
            self.winner = "白が勝ちました"
        elif model.winner == 3:
            self.winner = "引き分けです"
        print(self.winner)
