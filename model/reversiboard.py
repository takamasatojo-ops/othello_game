class ReversiBoard:

    def change_stone(self, x, y, turn, enemy, board):
        board[x][y] = turn
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
                elif board[nx][ny] == enemy:
                    while 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == enemy:
                        flips.append((nx, ny))
                        nx += dx
                        ny += dy
                        if not (0 <= nx < 8 and 0 <= ny < 8):
                            continue
                        elif board[nx][ny] == turn:
                            for px, py in flips:
                                board[px][py] = turn

    def search_putting_position(self, turn, enemy, board, valid_moves):
        valid_moves = set()
        for x in range(8):
            for y in range(8):
                if board[x][y] == 3:
                    board[x][y] = 0
        for x in range(8):
            for y in range(8):
                if board[x][y] == 1 or board[x][y] == 2:
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
                            elif board[nx][ny] == enemy:
                                while (
                                    0 <= nx < 8
                                    and 0 <= ny < 8
                                    and board[nx][ny] == enemy
                                ):
                                    nx += dx
                                    ny += dy
                                    if not (0 <= nx < 8 and 0 <= ny < 8):
                                        continue
                                    elif board[nx][ny] == turn:
                                        board[x][y] = 3
                                        valid_moves.add((x, y))
        return board, valid_moves
