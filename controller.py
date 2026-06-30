from model.model import ReversiModel
from model.model_cpu import ReversiModelCpu
from view import BoardView
from model.player import HumanPlayer


class ReversiController:
    def __init__(self):
        self.model = ReversiModel()
        self.view = BoardView()
        self.model_cpu = ReversiModelCpu()
        self.human_player = HumanPlayer()

    def run(self) -> None:
        input_partner = self.view.select_cpu_human()
        if input_partner == "human":
            while self.model.check_end_game is True:
                self.view.print_all(self.model)
                put_cell = self.view.change_stone()
                self.human_player.control_board(put_cell)
            self.view.end_game(self.model)
        elif input_partner == "CPU":
            human_stone = self.view.select_stone()
            if human_stone is None:
                self.view.print_correct_answer()
            else:
                while self.model_cpu.check_end_game is True:
                    self.view.print_all(self.model_cpu)
                    put_cell_cpu = self.view.change_stone_cpu(self.model_cpu, human_stone)
                    self.model_cpu.control_board_cpu(put_cell_cpu, human_stone)
                    self.view.print_cpu_select(self.model_cpu, human_stone)
                self.view.end_game(self.model_cpu)
        else:
            self.view.print_correct_answer()
