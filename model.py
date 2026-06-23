
class ReversiModel:
    def __init__(self):
        self.board = [
        ["･","･","･","･","･","･","･","･"],
        ["･","･","･","･","･","･","･","･"],
        ["･","･","･","･","*","･","･","･"],
        ["･","･","･","B","W","*","･","･"],
        ["･","･","*","W","B","･","･","･"],
        ["･","･","･","*","･","･","･","･"],
        ["･","･","･","･","･","･","･","･"],
        ["･","･","･","･","･","･","･","･"]
        ]
        
        self.turn = "B"
        self.enemy = "W"
        self.valid_moves = {(2,4),(3,5),(4,2),(5,3)}
        
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
                                print(flips)
                                print(px,py)
                                self.board[px][py]=self.turn
        self.search_putting_position()
        if self.valid_moves == set():
            self.search_putting_position()

        return self.board, self.turn
    
    def search_putting_position(self):
        self.valid_moves = set()
        self.turn = "W" if self.turn=="B" else "B"
        self.enemy="W" if self.turn=="B" else "B"
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == "*":
                    self.board[x][y] = "･"
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == "B" or self.board[x][y] == "W":
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
                                    print(x,y)
                                    print(nx,ny)
                                    nx+=dx
                                    ny+=dy
                                    if not (0 <= nx < 8 and 0 <= ny < 8):
                                        continue
                                    elif self.board[nx][ny] == self.turn:
                                        # print(self.turn)
                                        self.board[x][y] = "*"
                                        self.valid_moves.add((x,y))
                                        print(self.valid_moves)
            
        # print(self.valid_moves)
        return self.valid_moves
    

    


