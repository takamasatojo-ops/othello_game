from model.reversiboard import ReversiBoard

class Game:
    def __init__(self):
        self.reversi_board=ReversiBoard()
    
    def switch_turn(self, turn, enemy):
        turn = 2 if turn == 1 else 1
        enemy = 2 if turn == 1 else 1
        return turn, enemy

    def check_turn(self, valid_moves, turn, enemy, board):
        if valid_moves == set():
            # self.turn_pass=self.turn
            self.switch_turn(turn, enemy)
            self.reversi_board.search_putting_position(turn, enemy, board, valid_moves)
            if valid_moves == set():
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