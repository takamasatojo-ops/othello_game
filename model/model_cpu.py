import copy

from model.model import ReversiModel


class ReversiModelCpu(ReversiModel):
    def __init__(self):
        super().__init__(
            board=None,
            valid_moves=None,
            turn=None,
            enemy=None,
            check_end_game=None
        )
        self.minimax_depth = 3
        self.best_cpu_position = ""
        self.cpu_put_stone = False
        # 1は人間、２はCPU

    def control_board_cpu(self, put_cell, human_stone):
        self.check_input_cell_cpu(put_cell, human_stone)
        if self.check_input == 1:
            self.turn_pass = 0
            self.cpu_put_stone = False
            if self.turn == human_stone:
                x = self.x
                y = self.y
                self.human_control(x, y)
            else:
                self.cpu_control()
                self.cpu_put_stone = True
            self.check_turn()
        # self.check_turn()
        return (
            self.board,
            self.valid_moves,
            self.turn,
            self.enemy,
            self.check_end_game,
            self.turn_pass,
            self.check_input,
        )

    def cpu_control(self):
        self.select_cpu_position()
        x = self.x
        y = self.y
        self.change_stone(x, y)
        self.switch_turn()
        self.search_putting_position()

    def select_cpu_position(self):
        copied_model = copy.deepcopy(self)
        best_score = -float("inf")
        copied_cpu_turn = copied_model.turn
        minimax_depth = self.minimax_depth
        for cpu_position in list(copied_model.valid_moves):
            copied_model.change_stone(*cpu_position)
            copied_model.switch_turn()
            copied_model.search_putting_position()
            score = copied_model.minimax(
                copied_model, minimax_depth - 1, copied_cpu_turn, False
            )
            if score > best_score:
                best_score = score
                self.best_cpu_position = cpu_position
        self.x, self.y = map(int, self.best_cpu_position)
        return self.best_cpu_position

    def minimax(self, copied_model, minimax_depth, copied_cpu_turn, is_maximizing):
        if minimax_depth == 0 or copied_model.valid_moves == set():
            return self.evaluate_board(copied_model, copied_cpu_turn)

        if is_maximizing:
            best_score = -float("inf")
            for cpu_position in list(copied_model.valid_moves):
                copied_model.change_stone(*cpu_position)
                copied_model.switch_turn()
                copied_model.search_putting_position()

                score = copied_model.minimax(
                    copied_model, minimax_depth - 1, copied_cpu_turn, False
                )
                best_score = max(best_score, score)
            return best_score

        else:
            best_human_score = float("inf")
            for human_position in list(copied_model.valid_moves):
                copied_model.change_stone(*human_position)
                copied_model.switch_turn()
                copied_model.search_putting_position()

                score = copied_model.minimax(
                    copied_model, minimax_depth - 1, copied_cpu_turn, True
                )
                best_human_score = min(best_human_score, score)
            return best_human_score

    def check_input_cell_cpu(self, put_cell, human_stone):
        if self.turn == human_stone:
            try:
                row = int(put_cell[0])
                column = int(put_cell[1])
                answer = (row, column)
                if answer in self.valid_moves:
                    self.x = row
                    self.y = column
                    self.check_input = 1
                else:
                    self.check_input = 0
            except ValueError:
                self.check_input = 0
        else:
            if put_cell == "":
                self.check_input = 1
            else:
                self.check_input = 0
        return self.check_input

    def evaluate_board(self, copied_model, copied_cpu_turn):
        num_B = 0
        num_W = 0
        for x in range(8):
            for y in range(8):
                if copied_model.board[x][y] == 1:
                    num_B += 1
                elif copied_model.board[x][y] == 2:
                    num_W += 1
        #  引き分けは３とする
        if copied_cpu_turn == 1:
            return num_B - num_W
        else:
            return num_W - num_B
