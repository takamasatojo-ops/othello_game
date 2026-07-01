import copy


from model.reversiboard import ReversiBoard


class HumanPlayer:
    def __init__(self):
        self.check_input = 1
        self.x = 9
        self.y = 9

    def check_input_cell(self, put_cell, valid_moves):
        try:
            answer = tuple(map(int, put_cell.strip("()").split(",")))
        except ValueError:
            answer = None
        if answer in valid_moves:
            self.x, self.y = map(int, put_cell.strip("()").split(","))
            self.check_input = 1
        else:
            self.check_input = 0
        return self.check_input, self.x, self.y


class CpuPlayer:
    def __init__(self):
        self.reversi_board = ReversiBoard()
        self.minimax_depth = 3
        self.x = 9
        self.y = 9

    def select_cpu_position(self, whole_model):
        copied_model = copy.deepcopy(whole_model)
        best_score = -float("inf")
        copied_cpu_turn = copied_model.turn
        copied_cpu_enemy = copied_model.enemy
        minimax_depth = self.minimax_depth
        for cpu_position in list(copied_model.valid_moves):
            copied_model.reversi_board.change_stone(
                *cpu_position, copied_cpu_turn, copied_cpu_enemy
            )
            copied_model.switch_turn()
            copied_model.reversi_board.search_putting_position(
                copied_cpu_turn, copied_cpu_enemy
            )
            score = self.minimax(
                copied_model, minimax_depth - 1, copied_cpu_turn, False
            )
            if score > best_score:
                best_score = score
                self.best_cpu_position = cpu_position
        self.x, self.y = map(int, self.best_cpu_position)
        return self.best_cpu_position, self.x, self.y

    def minimax(self, copied_model, minimax_depth, copied_cpu_turn, is_maximizing):
        if minimax_depth == 0 or copied_model.valid_moves == set():
            return self.evaluate_board(copied_model, copied_cpu_turn)

        if is_maximizing:
            best_score = -float("inf")
            for cpu_position in list(copied_model.valid_moves):
                copied_cpu_enemy = copied_model.enemy
                copied_model.reversi_board.change_stone(
                    *cpu_position, copied_cpu_turn, copied_cpu_enemy
                )
                copied_model.switch_turn()
                copied_cpu_enemy = copied_model.enemy
                copied_model.reversi_board.search_putting_position(
                    copied_cpu_turn, copied_cpu_enemy
                )

                score = copied_model.minimax(
                    copied_model, minimax_depth - 1, copied_cpu_turn, False
                )
                best_score = max(best_score, score)
            return best_score

        else:
            best_human_score = float("inf")
            for human_position in list(copied_model.valid_moves):
                copied_cpu_enemy = copied_model.enemy
                copied_model.reversi_board.change_stone(
                    *human_position, copied_cpu_turn, copied_cpu_enemy
                )
                copied_model.game_cpu.switch_turn()
                copied_cpu_enemy = copied_model.enemy
                copied_model.reversi_board.search_putting_position(
                    copied_cpu_turn, copied_cpu_enemy
                )

                score = copied_model.minimax(
                    copied_model, minimax_depth - 1, copied_cpu_turn, True
                )
                best_human_score = min(best_human_score, score)
            return best_human_score

    def check_input_cell_cpu(self, turn, put_cell, human_stone, valid_moves):
        if turn == human_stone:
            try:
                answer = tuple(map(int, put_cell.strip("()").split(",")))
            except ValueError:
                answer = None
            if answer in valid_moves:
                self.x, self.y = map(int, put_cell.strip("()").split(","))
                self.check_input = 1
            else:
                self.check_input = 0
        else:
            if put_cell == "":
                self.check_input = 1
            else:
                self.check_input = 0
        return self.check_input, self.x, self.y

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
