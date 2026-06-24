from model import ReversiModel
from view import BoardView


class ReversiController:
    def __init__(self):
        self.model=ReversiModel()
        self.view=BoardView()
    
    def change_stone(self):
        #put_cellはstr型なのでtuple型へ変換
        put_cell=self.view.change_stone()
        self.model.control_board(put_cell)
            
    def run(self) -> None:
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
        