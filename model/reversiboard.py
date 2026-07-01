class ReversiBoard:
    def __init__(self, board=None, valid_moves=None):
        if board is None:
            self.board = self.init_board()
        else:
            self.board = board
        if valid_moves is None:
            self.valid_moves = self.init_valid_move()
        else:
            self.valid_moves = valid_moves

    def init_board(self):
        # 黒が１、白が２、何もないマスが0、自分の石を置けるマスが３
        return [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 1, 2, 3, 0, 0],
            [0, 0, 3, 2, 1, 0, 0, 0],
            [0, 0, 0, 3, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def init_valid_move(self):
        return {(2, 4), (3, 5), (4, 2), (5, 3)}
        # 黒が１、白が２、何もないマスが0、自分の石を置けるマスが３

    def change_stone(self, x, y, turn, enemy):
        self.board[x][y] = turn
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
                elif self.board[nx][ny] == enemy:
                    while 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == enemy:
                        flips.append((nx, ny))
                        nx += dx
                        ny += dy
                        if not (0 <= nx < 8 and 0 <= ny < 8):
                            continue
                        elif self.board[nx][ny] == turn:
                            for px, py in flips:
                                self.board[px][py] = turn
        return self.board

    def search_putting_position(self, turn, enemy):
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
                            elif self.board[nx][ny] == enemy:
                                while (
                                    0 <= nx < 8
                                    and 0 <= ny < 8
                                    and self.board[nx][ny] == enemy
                                ):
                                    nx += dx
                                    ny += dy
                                    if not (0 <= nx < 8 and 0 <= ny < 8):
                                        continue
                                    elif self.board[nx][ny] == turn:
                                        self.board[x][y] = 3
                                        self.valid_moves.add((x, y))
        return self.board, self.valid_moves
