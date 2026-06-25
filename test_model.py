# import unittest
from model import ReversiModel
import pytest

@pytest.mark.parametrize(
    "board,valid_moves,turn,enemy,put_cell,check_end_game,expected_board,expected_valid_moves,expected_turn,expected_enemy,expected_check_end_game",
    [
        #最初の状態から1手
        (
            [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,3,0,0,0],
            [0,0,0,1,2,3,0,0],
            [0,0,3,2,1,0,0,0],
            [0,0,0,3,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
            ],
            {(2,4),(3,5),(4,2),(5,3)},
            1,
            2,
            "(4,2)",
            True,
            [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,3,1,2,0,0,0],
            [0,0,1,1,1,0,0,0],
            [0,0,3,0,3,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
            ],
            {(3,2),(5,2),(5,4)},
            2,
            1,
            True
        ),
        #白がパスになるパターン
        (
            [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,3,1,1,0],
            [1,1,3,1,2,3,1,1],
            [1,1,3,2,1,1,1,1],
            [1,1,3,3,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1]
            ],
            {(4,2),(2,4),(3,5),(4,2),(5,3),(5,2)},
            1,
            2,
            "(3,5)",
            True,
            [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,0,1,1,0],
            [1,1,3,1,1,1,1,1],
            [1,1,3,2,1,1,1,1],
            [1,1,3,3,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1]
            ],
            {(3,2),(4,2),(5,3),(5,2)},
            1,
            2,
            True,
        ),
        #ゲーム終了パターン
        (
            [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,2,1,1,3],
            [1,1,2,1,2,2,1,1],
            [1,1,2,2,1,1,1,1],
            [1,1,2,2,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1]
            ],
            {(2,7)},
            2,
            1,
            "(2,7)",
            True,
            [
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,2,2,2,2],
            [1,1,2,1,2,2,1,1],
            [1,1,2,2,1,1,1,1],
            [1,1,2,2,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1]
            ],
            set(),
            2,
            1,
            False,
        )
    ]
)

def test_control_board(
    board:list,
    valid_moves:tuple,
    turn:int,
    enemy:int,
    put_cell:str,
    check_end_game:bool,
    expected_board:list,
    expected_valid_moves:tuple,
    expected_turn:int,
    expected_enemy:int,
    expected_check_end_game:bool
    ):
    rm=ReversiModel(board,valid_moves,turn,enemy,check_end_game)
    assert rm.control_board(put_cell)==(
        expected_board,
        expected_valid_moves,
        expected_turn,
        expected_enemy,
        expected_check_end_game
        )

# @pytest.mark.parametrize(
#     "put_cell,x,y",
#     [
#         ("(4,2)",4,2),
#         # (2,4,3,4),
#     ]
# )

# def test_check_input_cell(put_cell:str, x:int, y:int):
#     assert rm.check_input_cell(put_cell) == (x,y)
    
    
# @pytest.mark.parametrize(
#     "x,y,nx,ny",
#     [
#         (4,2,4,3),
#         # (2,4,3,4),
#     ]
# )

# #ひっくり返す対象が正しいか
# def test_change_stone(x:int, y:int, nx:int, ny:int):
#     assert rm.change_stone(x,y) == (nx,ny)


# @pytest.mark.parametrize(
#     "board,valid_moves,turn",
#         [
#             (
#             [
#             [0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0],
#             [0,0,3,1,2,0,0,0],
#             [0,0,1,1,1,0,0,0],
#             [0,0,3,0,3,0,0,0],
#             [0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0]
#             ],
#         {(3,2),(5,2),(5,4)},
#         2
#             )
#         ]
#     )
    
# def test_search_putting_position(board:list, valid_moves:tuple, turn:int):
#     assert rm.search_putting_position() == (board,valid_moves, turn)
    



# class TestModel(unittest.TestCase):
#     def __init__(self):
#         pass
    
#     def test_model(self):
#         reversi_model=ReversiModel()
#         self.assertEqual(reversi_model.change_stone.(4,2))