import tkinter as tk

from typing import Protocol

class ModelHandler(Protocol):
    def control_board(self, input_row, input_column) -> None:
        ...

class WindowView():
    NUM_CELL=8

    BOARD_COLOR = 'green'
    BOARD_COLOR = 'green' # 盤面の背景色
    YOUR_COLOR = 'black'
    COM_COLOR = 'white'
    PLACABLE_COLOR = 'yellow' # 次に石を置ける場所を示す色
    MARGIN = 10 # 余白スペース
    STONE_MARGIN = 5

    CELL_WIDTH = 50
    CELL_HEIGHT = 50

    BOARD_WIDTH=CELL_WIDTH*8+MARGIN*2
    BOARD_HEIGHT=CELL_HEIGHT*8+MARGIN*2
    
    def __init__(self, model_handler:ModelHandler):
        self.app = tk.Tk()
        self.app.title("オセロゲーム")
        self.app.geometry("600x500")
        self.app.config(bg="white")
        self.canvas = tk.Canvas(
            bg=self.BOARD_COLOR,
            width=self.BOARD_WIDTH,
            height=self.BOARD_HEIGHT,
            highlightthickness=0
        )
        
        self.canvas.pack()
        self.canvas.bind('<ButtonPress>', self.click)
        self.current_turn = tk.Label(self.app, text="現在のターンは黒です")
        self.current_turn.pack()
        self.model_handler=model_handler
        
    def click(self, event):
        input_column=(event.x-self.MARGIN)//self.CELL_WIDTH
        input_row=(event.y-self.MARGIN)//self.CELL_HEIGHT
        self.model_handler.control_board(input_row,input_column)

    def flash(self, model):
        for y in range(self.MARGIN, self.MARGIN + self.CELL_WIDTH * self.NUM_CELL + 1, self.CELL_WIDTH):
            self.canvas.create_line(self.MARGIN, y, self.MARGIN + self.CELL_WIDTH * self.NUM_CELL, y)
        for x in range(self.MARGIN, self.MARGIN + self.CELL_HEIGHT * self.NUM_CELL + 1,self.CELL_HEIGHT):
            self.canvas.create_line(x, self.MARGIN, x, self.MARGIN + self.CELL_HEIGHT * self.NUM_CELL)
        
        for x in range(8):
            for y in range(8):
                if model.board[x][y] == 1:
                    self.canvas.create_oval(
                        x*self.CELL_WIDTH+self.MARGIN+self.STONE_MARGIN,
                        y*self.CELL_HEIGHT+self.MARGIN+self.STONE_MARGIN,
                        (x+1)*self.CELL_WIDTH+self.MARGIN-self.STONE_MARGIN,
                        (y+1)*self.CELL_HEIGHT+self.MARGIN-self.STONE_MARGIN,
                        fill="black"
                    )
                elif model.board[x][y] == 2:
                    self.canvas.create_oval(
                        x*self.CELL_WIDTH+self.MARGIN+self.STONE_MARGIN,
                        y*self.CELL_HEIGHT+self.MARGIN+self.STONE_MARGIN,
                        (x+1)*self.CELL_WIDTH+self.MARGIN-self.STONE_MARGIN,
                        (y+1)*self.CELL_HEIGHT+self.MARGIN-self.STONE_MARGIN,
                        fill="white"
                    )
                elif model.board[x][y] == 3:
                    self.canvas.create_rectangle(
                        x*self.CELL_WIDTH+self.MARGIN,
                        y*self.CELL_HEIGHT+self.MARGIN,
                        (x+1)*self.CELL_WIDTH+self.MARGIN,
                        (y+1)*self.CELL_HEIGHT+self.MARGIN,
                        fill="yellow",
                    )
                else:
                    pass
        
    def update_current_turn(self):
        self.current_turn = tk.Label(self.app, text="現在のターンは白です")

