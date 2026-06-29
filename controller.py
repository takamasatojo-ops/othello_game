from model import ReversiModel
from model_cpu import ReversiModelCpu
from view import BoardView


class ReversiController:
    def __init__(self):
        self.model=ReversiModel()
        self.view=BoardView()
        self.model_cpu=ReversiModelCpu()
    
    def change_stone(self):
        put_cell=self.view.change_stone()
        self.model.control_board(put_cell)
        
    def select_stone(self):
        select_stone=self.view.select_stone()
        if select_stone=="black":
            human_stone=1
        elif select_stone=="white":
            human_stone=2
        else:
            human_stone=None
        return human_stone

        
    def run(self) -> None:
        input_partner=self.view.select_cpu_human()
        if input_partner=="human":
            while self.model.check_end_game==True:
                model_board=self.model.board
                model_turn=self.model.turn
                model_valid_moves=self.model.valid_moves
                model_check_input=self.model.check_input
                self.view.print_all(model_board,model_turn,model_valid_moves,model_check_input)
                self.change_stone()
            model_board=self.model.board
            model_winner=self.model.winner
            model_num_B=self.model.num_B
            model_num_W=self.model.num_W
            self.view.end_game(model_board, model_winner, model_num_B, model_num_W)
        elif input_partner=="CPU":
            human_stone=self.select_stone()
            while self.model_cpu.check_end_game==True:
                model_cpu_board=self.model_cpu.board
                model_cpu_turn=self.model_cpu.turn
                model_cpu_valid_moves=self.model_cpu.valid_moves
                model_cpu_check_input=self.model_cpu.check_input
                self.view.print_all_cpu(model_cpu_board,model_cpu_turn,model_cpu_valid_moves,model_cpu_check_input)
                if self.model_cpu.turn==human_stone:
                    put_cell=self.view.change_stone()
                else:
                    put_cell=self.view.cpu_put_stone()
                check_input=self.model_cpu.check_input_cell_cpu(put_cell,human_stone)
                if check_input==1:
                    self.model_cpu.control_board_cpu(put_cell,human_stone)
                else:
                    self.view.print_correct_answer()
            model_board=self.model_cpu.board
            model_winner=self.model_cpu.winner
            model_num_B=self.model_cpu.num_B
            model_num_W=self.model_cpu.num_W
            self.view.end_game(model_board, model_winner, model_num_B, model_num_W)
        else:
            self.view.print_correct_answer()
        