class Game:
    def __init__(
        self,
        valid_moves=None,
        turn=None,
        enemy=None,
        check_end_game=None
    ):
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
        self.turn_pass=0
        self.num_B = 0
        self.num_W = 0
        self.winner = 1
        self.x = 9
        self.y = 9
        self.check_input = 1
        
    def init_valid_move(self):
        return {(2, 4), (3, 5), (4, 2), (5, 3)}
        # 黒が１、白が２、何もないマスが0、自分の石を置けるマスが３

    def init_turn(self):
        return 1

    def init_enemy(self):
        return 2

    def init_check_end_game(self):
        return True
    def switch_turn(self):
        self.turn = 2 if self.turn == 1 else 1
        self.enemy = 2 if self.turn == 1 else 1
        
    def check_turn(self,):
        if self.valid_moves == set():
            self.turn_pass=self.turn
            self.switch_turn()
            self.search_putting_position()
            if self.valid_moves == set():
                self.check_end_game = False
                self.calculate_stone()
                
    def calculate_stone(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 1:
                    self.num_B += 1
                elif self.board[x][y] == 2:
                    self.num_W += 1
        if self.num_B > self.num_W:
            self.winner = 1
        elif self.num_W > self.num_B:
            self.winner = 2
        elif self.num_B == self.num_W:
            self.winner = 3
        #  引き分けは３とする
        return self.winner, self.num_B, self.num_W