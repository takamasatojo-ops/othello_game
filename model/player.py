import copy

from model.game import Game
from model.reversiboard import ReversiBoard


class HumanPlayer:
    def __init__(
        self, board=None, valid_moves=None, turn=None, enemy=None, check_end_game=None
    ):
        self.game = Game()
        self.reversi_board = ReversiBoard()

        if board is None:
            self.board = self.init_board()
        else:
            self.board = board
        if valid_moves is None:
            self.valid_moves = self.init_valid_move()
        else:
            self.valid_moves = valid_moves
        if turn is None:
            self.turn = self.init_turn()
        else:
            self.turn = turn
        if enemy is None:
            self.enemy = self.init_enemy()
        else:
            self.enemy = enemy
        if check_end_game is None:
            self.check_end_game = self.init_check_end_game()
        else:
            self.check_end_game = check_end_game
        self.turn_pass = 0
        self.num_B = 0
        self.num_W = 0
        self.winner = 1
        self.x = 9
        self.y = 9
        self.check_input = 1

    def init_board(self):
        # 黒が１、白が２、何もないマスが0、自分の石を置けるマスが３
        return [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 3, 1, 1, 0],
            [1, 1, 0, 1, 2, 3, 1, 1],
            [1, 1, 3, 2, 1, 1, 1, 0],
            [1, 1, 0, 3, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def init_valid_move(self):
        return {(2, 4), (3, 5), (4, 2), (5, 3)}
        # 黒が１、白が２、何もないマスが0、自分の石を置けるマスが３

    def init_turn(self):
        return 1

    def init_enemy(self):
        return 2

    def init_check_end_game(self):
        return True

    def control_board(self, put_cell):
        self.check_input_cell(put_cell)
        if self.check_input == 1:
            self.turn_pass = 0
            self.human_control(
                self.x, self.y, self.turn, self.enemy, self.board, self.valid_moves
            )
            self.game.check_turn(self.valid_moves, self.turn, self.enemy, self.board)
        return self.board, self.valid_moves, self.turn, self.enemy, self.check_input
        # self.game.check_end_game, \
        # self.turn_pass, \

    def check_input_cell(self, put_cell):
        try:
            answer = tuple(map(int, put_cell.strip("()").split(",")))
        except ValueError:
            answer = None
        if answer in self.valid_moves:
            self.x, self.y = map(int, put_cell.strip("()").split(","))
            self.check_input = 1
        else:
            self.check_input = 0
        return self.check_input

    def human_control(self, x, y, turn, enemy, board, valid_moves):
        self.reversi_board.change_stone(x, y, turn, enemy, board)
        self.game.switch_turn(turn, enemy)
        self.reversi_board.search_putting_position(turn, enemy, board, valid_moves)


# class MiniMaxPlayer:
#     def __init__(self):
#         self.game = Game()
#         self.reversi_board = Board()

#         self.minimax_depth = 3
#         self.best_cpu_position = ""
#         self.cpu_put_stone=False

#     def control_board_cpu(self, put_cell, human_stone):
#         self.check_input_cell_cpu(put_cell,human_stone)
#         if self.check_input == 1:
#             self.turn_pass = 0
#             self.cpu_put_stone = False
#             if self.game.turn == human_stone:
#                 x=self.x
#                 y=self.y
#                 self.human_control(x, y)
#             else:
#                 self.cpu_control()
#                 self.cpu_put_stone = True
#             self.game.check_turn()
#         # self.check_turn()
#         return (
#             self.reversi_board.board,
#             self.reversi_board.valid_moves,
#             self.game.turn,
#             self.game.enemy,
#             self.game.check_end_game,
#             self.turn_pass,
#             self.check_input
#         )

#     def cpu_control(self):
#         self.select_cpu_position()
#         x = self.x
#         y = self.y
#         self.reversi_board.change_stone(x, y)
#         self.game.switch_turn()
#         self.reversi_board.search_putting_position()

#     def select_cpu_position(self):
#         copied_model = copy.deepcopy(self)
#         best_score = -float("inf")
#         copied_cpu_turn = copied_model.game.turn
#         minimax_depth = self.minimax_depth
#         for cpu_position in list(copied_model.board.valid_moves):
#             copied_model.board.change_stone(*cpu_position)
#             copied_model.game.switch_turn()
#             copied_model.board.search_putting_position()
#             score = copied_model.minimax(
#                 copied_model, minimax_depth - 1, copied_cpu_turn, False
#             )
#             if score > best_score:
#                 best_score = score
#                 self.best_cpu_position = cpu_position
#         self.x, self.y = map(int, self.best_cpu_position)

#     def minimax(self, copied_model, minimax_depth, copied_cpu_turn, is_maximizing):
#         if minimax_depth == 0 or copied_model.valid_moves == set():
#             return self.evaluate_board(copied_model, copied_cpu_turn)

#         if is_maximizing:
#             best_score = -float("inf")
#             for cpu_position in list(copied_model.valid_moves):
#                 copied_model.change_stone(*cpu_position)
#                 copied_model.switch_turn()
#                 copied_model.search_putting_position()

#                 score = copied_model.minimax(
#                     copied_model, minimax_depth - 1, copied_cpu_turn, False
#                 )
#                 best_score = max(best_score, score)
#             return best_score

#         else:
#             best_human_score = float("inf")
#             for human_position in list(copied_model.valid_moves):
#                 copied_model.change_stone(*human_position)
#                 copied_model.switch_turn()
#                 copied_model.search_putting_position()

#                 score = copied_model.minimax(
#                     copied_model, minimax_depth - 1, copied_cpu_turn, True
#                 )
#                 best_human_score = min(best_human_score, score)
#             return best_human_score

#     def check_input_cell_cpu(self, put_cell, human_stone):
#         if self.game.turn == human_stone:
#             try:
#                 answer = tuple(map(int, put_cell.strip("()").split(",")))
#             except ValueError:
#                 answer = None
#             if answer in self.reversi_board.valid_moves:
#                 self.x, self.y = map(int, put_cell.strip("()").split(","))
#                 self.check_input = 1
#             else:
#                 self.check_input = 0
#         else:
#             if put_cell == "":
#                 self.check_input = 1
#             else:
#                 self.check_input = 0
#         return self.check_input

#     def evaluate_board(self, copied_model, copied_cpu_turn):
#         num_B = 0
#         num_W = 0
#         for x in range(8):
#             for y in range(8):
#                 if copied_model.board[x][y] == 1:
#                     num_B += 1
#                 elif copied_model.board[x][y] == 2:
#                     num_W += 1
#         #  引き分けは３とする
#         if copied_cpu_turn == 1:
#             return num_B - num_W
#         else:
#             return num_W - num_B
