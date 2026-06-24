
class ReversiModel:
    def __init__(self):
        self.board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,3,0,0,0],
        [0,0,0,1,2,3,0,0],
        [0,0,3,2,1,0,0,0],
        [0,0,0,3,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]
        
        
        # 黒が１、白が２、何もないマスが0、自分の石を置けるますが３
        self.turn = 1
        self.enemy = 2
        self.valid_moves = {(2,4),(3,5),(4,2),(5,3)}
        self.check_end_game=True
        
    def change_stone(self,x,y):
        self.board[x][y]=self.turn
        for dx in -1,0,1:
            for dy in -1,0,1:
                nx=x+dx
                ny=y+dy
                #ひっくり返す候補
                flips=[]
                if dx==0 and dy == 0:
                    continue
                elif not (0 <= nx < 8 and 0 <= ny < 8):
                    continue
                elif self.board[nx][ny] == self.enemy:
                    while 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == self.enemy:
                        flips.append((nx,ny))
                        nx+=dx
                        ny+=dy
                        if not (0 <= nx < 8 and 0 <= ny < 8):
                            continue
                        elif self.board[nx][ny] == self.turn:
                            for px, py in flips:
                                # print(flips)
                                # print(px,py)
                                self.board[px][py]=self.turn
    
    def search_putting_position(self):
        self.valid_moves = set()
        self.turn = 2 if self.turn==1 else 1
        self.enemy=2 if self.turn==1 else 1
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 3:
                    self.board[x][y] = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 1 or self.board[x][y] == 2:
                    continue
                else:
                    for dx in -1,0,1:
                        for dy in -1,0,1:
                            nx=x+dx
                            ny=y+dy
                            if dx==0 and dy == 0:
                                continue
                            elif not (0 <= nx < 8 and 0 <= ny < 8):
                                continue
                            elif  self.board[nx][ny] == self.enemy:
                                while 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == self.enemy:
                                    # print(self.enemy)
                                    # print(x,y)
                                    # print(x,y)
                                    # print(nx,ny)
                                    nx+=dx
                                    ny+=dy
                                    if not (0 <= nx < 8 and 0 <= ny < 8):
                                        continue
                                    elif self.board[nx][ny] == self.turn:
                                        # print(self.turn)
                                        self.board[x][y] = 3
                                        self.valid_moves.add((x,y))
                                        # print(self.valid_moves)
        return self.board, self.valid_moves, self.turn
                                        
    def calculate_stone(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 1:
                    self.num_B+=1
                elif self.board[x][y] == 2:
                    self.num_W+=1
        
        if self.num_B>self.num_W:
            self.winner=1
        elif self.num_W>self.num_B:
            self.winner=2
        elif self.num_B == self.num_W:
            self.winner=3
        #  引き分けは３とする
        return self.winner, self.num_B, self.num_W
    




