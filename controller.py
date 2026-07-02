from model.model import ReversiModel
from model.model_cpu import ReversiModelCpu
from view import BoardView
from model.game import GameHuman, GameCpu
from view_window import WindowView


class ReversiController:
    def __init__(self):
        self.model = ReversiModel()
        self.view = BoardView()
        self.model_cpu = ReversiModelCpu()
        self.game_human = GameHuman()
        self.game_cpu = GameCpu()
        self.window_view = WindowView()

    def run(self) -> None:
        self.window_view.flash(self.model)
        self.window_view.app.mainloop()
        
# class ReversiController:
#     def __init__(self):
#         self.model = ReversiModel()
#         self.view = BoardView()
#         self.model_cpu = ReversiModelCpu()
#         self.game_human = GameHuman()
#         self.game_cpu = GameCpu()

    # def run(self) -> None:
    #     input_partner = self.view.select_cpu_human()
    #     if input_partner == "1":
    #         while self.model.check_end_game is True:
    #             self.view.print_all(self.model)
    #             input_row, input_column = self.view.change_stone()
    #             self.model.control_board(input_row, input_column)
    #         self.view.end_game(self.model)
    #     elif input_partner == "2":
    #         human_stone = self.view.select_stone()
    #         if human_stone is None:
    #             self.view.print_correct_answer()
    #         else:
    #             while self.model_cpu.check_end_game is True:
    #                 self.view.print_all(self.model_cpu)
    #                 put_cell_cpu = self.view.change_stone_cpu(
    #                     self.model_cpu, human_stone
    #                 )
    #                 self.model_cpu.control_board_cpu(put_cell_cpu, human_stone)
    #                 self.view.print_cpu_select(self.model_cpu)
    #             self.view.end_game(self.model_cpu)
    #     else:
    #         self.view.print_correct_answer()







    # def run(self) -> None:
    #     input_partner = self.view.select_cpu_human()
    #     if input_partner == "human":
    #         while self.game_human.check_end_game is True:
    #             self.view.print_all(self.game_human)
    #             put_cell = self.view.change_stone()
    #             self.game_human.control_board(put_cell)
    #         self.view.end_game(self.game_human)
    #     elif input_partner == "CPU":
    #         human_stone = self.view.select_stone()
    #         if human_stone is None:
    #             self.view.print_correct_answer()
    #         else:
    #             while self.game_cpu.check_end_game is True:
    #                 self.view.print_all(self.game_cpu)
    #                 put_cell_cpu = self.view.change_stone_cpu(
    #                     self.game_cpu, human_stone
    #                 )
    #                 self.game_cpu.control_board_cpu(put_cell_cpu, human_stone)
    #                 self.view.print_cpu_select(self.game_cpu, human_stone)
    #             self.view.end_game(self.game_cpu)
    #     else:
    #         self.view.print_correct_answer()
