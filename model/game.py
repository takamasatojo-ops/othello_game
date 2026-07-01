import copy

from model.reversiboard import ReversiBoard
from model.player import HumanPlayer, CpuPlayer


class GameHuman:
    def __init__(self, turn=None, enemy=None, check_end_game=None):
        self.reversi_board = ReversiBoard()
        self.human_player = HumanPlayer()
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
        self.board = self.reversi_board.board
        self.valid_moves = self.reversi_board.valid_moves
        self.check_input = 1

    def init_turn(self):
        return 1

    def init_enemy(self):
        return 2

    def init_check_end_game(self):
        return True

    def control_board(self, put_cell):
        self.human_player.check_input_cell(put_cell, self.reversi_board.valid_moves)
        self.check_input = self.human_player.check_input
        if self.human_player.check_input == 1:
            x = self.human_player.x
            y = self.human_player.y
            self.turn_pass = 0
            self.human_control(x, y)
            self.check_turn()
        self.board = self.reversi_board.board
        self.valid_moves = self.reversi_board.valid_moves
        return (
            self.board,
            self.valid_moves,
            self.turn,
            self.enemy,
            self.check_end_game,
            self.turn_pass,
            self.check_input,
        )

    def human_control(self, x, y):
        self.reversi_board.change_stone(x, y, self.turn, self.enemy)
        self.switch_turn()
        self.reversi_board.search_putting_position(self.turn, self.enemy)

    def switch_turn(self):
        self.turn = 2 if self.turn == 1 else 1
        self.enemy = 2 if self.turn == 1 else 1

    def check_turn(self):
        if self.reversi_board.valid_moves == set():
            self.turn_pass = self.turn
            self.switch_turn()
            self.reversi_board.search_putting_position(self.turn, self.enemy)
            if self.reversi_board.valid_moves == set():
                self.check_end_game = False
                self.calculate_stone()

    def calculate_stone(self):
        for x in range(8):
            for y in range(8):
                if self.reversi_board.board[x][y] == 1:
                    self.num_B += 1
                elif self.reversi_board.board[x][y] == 2:
                    self.num_W += 1
        if self.num_B > self.num_W:
            self.winner = 1
        elif self.num_W > self.num_B:
            self.winner = 2
        elif self.num_B == self.num_W:
            self.winner = 3
        #  引き分けは３とする
        return self.winner, self.num_B, self.num_W


class GameCpu(GameHuman):
    def __init__(self):
        super().__init__(turn=None, enemy=None, check_end_game=None)
        self.minimax_depth = 3
        self.best_cpu_position = ""
        self.cpu_put_stone = False
        self.cpu_player = CpuPlayer()
        # 1は人間、２はCPU

    def control_board_cpu(self, put_cell, human_stone):
        self.cpu_player.check_input_cell_cpu(
            self.turn, put_cell, human_stone, self.valid_moves
        )
        self.check_input = self.cpu_player.check_input
        if self.check_input == 1:
            self.turn_pass = 0
            self.cpu_put_stone = False
            if self.turn == human_stone:
                x = self.cpu_player.x
                y = self.cpu_player.y
                self.human_control(x, y)
            else:
                self.cpu_control()
                self.cpu_put_stone = True
            self.check_turn()
        self.board = self.reversi_board.board
        self.valid_moves = self.reversi_board.valid_moves
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
        whole_model = copy.deepcopy(self)
        self.cpu_player.select_cpu_position(whole_model)
        x = self.cpu_player.x
        y = self.cpu_player.y
        self.reversi_board.change_stone(x, y, self.turn, self.enemy)
        self.switch_turn()
        self.reversi_board.search_putting_position(self.turn, self.enemy)
