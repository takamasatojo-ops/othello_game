class ReversiModel:
    def __init__(
        self, board=None, valid_moves=None, turn=None, enemy=None, check_end_game=None
    ):
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
            x = self.x
            y = self.y
            self.turn_pass = 0
            self.human_control(x, y)
            self.check_turn()
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
        self.change_stone(x, y)
        self.switch_turn()
        self.search_putting_position()

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

    def change_stone(self, x, y):
        self.board[x][y] = self.turn
        for dx in -1, 0, 1:
            for dy in -1, 0, 1:
                nx = x + dx
                ny = y + dy
                # ひっくり返す候補
                flips = []
                if dx == 0 and dy == 0:
                    continue
                elif not (0 <= nx < 8 and 0 <= ny < 8):
                    continue
                elif self.board[nx][ny] == self.enemy:
                    while (
                        0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == self.enemy
                    ):
                        flips.append((nx, ny))
                        nx += dx
                        ny += dy
                        if not (0 <= nx < 8 and 0 <= ny < 8):
                            continue
                        elif self.board[nx][ny] == self.turn:
                            for px, py in flips:
                                self.board[px][py] = self.turn

    def switch_turn(self):
        self.turn = 2 if self.turn == 1 else 1
        self.enemy = 2 if self.turn == 1 else 1

    def search_putting_position(self):
        self.valid_moves = set()
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 3:
                    self.board[x][y] = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 1 or self.board[x][y] == 2:
                    continue
                else:
                    for dx in -1, 0, 1:
                        for dy in -1, 0, 1:
                            nx = x + dx
                            ny = y + dy
                            if dx == 0 and dy == 0:
                                continue
                            elif not (0 <= nx < 8 and 0 <= ny < 8):
                                continue
                            elif self.board[nx][ny] == self.enemy:
                                while (
                                    0 <= nx < 8
                                    and 0 <= ny < 8
                                    and self.board[nx][ny] == self.enemy
                                ):
                                    nx += dx
                                    ny += dy
                                    if not (0 <= nx < 8 and 0 <= ny < 8):
                                        continue
                                    elif self.board[nx][ny] == self.turn:
                                        self.board[x][y] = 3
                                        self.valid_moves.add((x, y))
        return self.board, self.valid_moves, self.turn, self.enemy

    def check_turn(self):
        if self.valid_moves == set():
            self.turn_pass = self.turn
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
