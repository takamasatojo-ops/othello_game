import copy

from model import ReversiModel


class ReversiModelCpu(ReversiModel):
    def __init__(self):
        super().__init__(board=None,valid_moves=None,turn=None,enemy=None,check_end_game=None)
        self.minimax_depth=3
        self.best_cpu_position=""
        #1は人間、２はCPU
    
    # CPUが黒の時に最初に実行
    def start_CPU(self):
        self.select_cpu_position()
        x=self.x
        y=self.y
        self.change_stone(x,y)
        self.switch_turn()
        self.search_putting_position_cpu()
        
    def control_board_cpu(self,put_cell,human_stone):
        if self.turn==human_stone:
            self.human_control(put_cell)
        else:
            self.cpu_control()
        
        if self.valid_moves == set():
            self.switch_turn()
            self.search_putting_position_cpu()
            if self.valid_moves == set():
                self.check_end_game = False
                self.calculate_stone()
        # self.check_turn()
        return self.best_cpu_position, self.board_before_cpu, self.board, self.valid_moves, self.turn, self.enemy,self.check_end_game
    
    def cpu_control(self):
        self.select_cpu_position()
        x=self.x
        y=self.y
        self.change_stone(x,y)
        self.switch_turn()
        self.search_putting_position_cpu()
    
    def human_control(self,put_cell):
        self.check_input_cell(put_cell)
        x=self.x
        y=self.y
        self.change_stone(x,y)
        self.switch_turn()
        self.search_putting_position_cpu()
        self.board_before_cpu=copy.deepcopy(self.board)
        self.valid_moves_before_cpu=self.valid_moves.copy()
        self.cpu_turn=self.turn
        
    def switch_turn(self):
        self.turn =2 if self.turn==1 else 1
        self.enemy=2 if self.turn==1 else 1
        
    def search_putting_position_cpu(self):
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
                                    nx+=dx
                                    ny+=dy
                                    if not (0 <= nx < 8 and 0 <= ny < 8):
                                        continue
                                    elif self.board[nx][ny] == self.turn:
                                        self.board[x][y] = 3
                                        self.valid_moves.add((x,y))
        return self.board, self.valid_moves, self.turn, self.enemy
        
    def select_cpu_position(self):
        copied_model=copy.deepcopy(self)
        best_score=-float("inf")
        copied_cpu_turn=copied_model.turn
        minimax_depth=self.minimax_depth
        for cpu_position in list(copied_model.valid_moves):
            copied_model.change_stone(*cpu_position)
            copied_model.switch_turn()
            copied_model.search_putting_position_cpu()
            score=copied_model.minimax(copied_model, minimax_depth-1, copied_cpu_turn, False)
            
            if score>best_score:
                best_score=score
                self.best_cpu_position=cpu_position
        self.x,self.y=map(int, self.best_cpu_position)
            
    def minimax(self, copied_model, minimax_depth, copied_cpu_turn, is_maximizing):
        if minimax_depth==0 or copied_model.valid_moves==set():
            return self.evaluate_board(copied_model,copied_cpu_turn)
        
        if is_maximizing:
            best_score=-float("inf")
            for cpu_position in list(copied_model.valid_moves):
                copied_model.change_stone(*cpu_position)
                copied_model.switch_turn()
                copied_model.search_putting_position_cpu()
                
                score=copied_model.minimax(copied_model, minimax_depth-1, copied_cpu_turn, False)
                best_score=max(best_score, score)
            return best_score
        
        else:
            best_human_score=float("inf")
            for human_position in list(copied_model.valid_moves):
                copied_model.change_stone(*human_position)
                copied_model.switch_turn()
                copied_model.search_putting_position_cpu()
                
                score=copied_model.minimax(copied_model, minimax_depth-1, copied_cpu_turn, True)
                best_human_score=min(best_human_score, score)
            return best_human_score
        
    def check_input_cell_cpu(self,put_cell,human_stone):
        if self.turn==human_stone:
            try:
                answer = tuple(map(int, put_cell.strip("()").split(",")))
            except ValueError:
                answer = None
            if answer in self.valid_moves:
                self.x,self.y=map(int, put_cell.strip("()").split(","))
                self.check_input=1
            else:
                self.check_input=0
        else:
            if put_cell=="":
                self.check_input=1
            else:
                self.check_input=0
        return self.check_input
                
    def evaluate_board(self, copied_model,copied_cpu_turn):
        num_B=0
        num_W=0
        for x in range(8):
            for y in range(8):
                if copied_model.board[x][y] == 1:
                    num_B+=1
                elif copied_model.board[x][y] == 2:
                    num_W+=1
        #  引き分けは３とする
        if copied_cpu_turn==1:
            return num_B-num_W
        else:
            return num_W-num_B
    
