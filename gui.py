from PyQt5.QtWidgets import (QWidget, QPushButton)
import threading
import time


class Game(QWidget):

    def __init__(self, w, h, cells, timer):
        # init vars
        self.w = w
        self.h = h
        self.buttons = [[None for j in range(self.w)] for i in range(self.h)]
        self.cells = cells
        # init ui
        super().__init__()
        self.init_ui()
        # start polling
        t = threading.Thread(target=self.get_next, args=(timer,))
        t.start()

    def get_next(self, timer):
        while True:
            print("get next")
            cells_new = self.cells.get_next()
            self.redraw(cells_new)
            self.update()
            time.sleep(timer)

    def button_clicked(self):
        sender = self.sender()
        tip = sender.toolTip()
        x, y = tip.split(':')
        self.cells.set_cell(int(x), int(y))
        sender.setStyleSheet("background-color: blue")

    def init_ui(self):
        for x in range(self.w):
            for y in range(self.h):
                btn = QPushButton('', self)
                btn.setToolTip(str(x) + ":" + str(y))
                btn.move(x*20, y*20)
                btn.resize(20, 20)
                btn.setStyleSheet("background-color: white")
                btn.clicked.connect(self.button_clicked)
                # noinspection PyTypeChecker
                self.buttons[x][y] = btn

        self.setGeometry(20*self.w+100, 20*self.h+100, 20*self.w, 20*self.h)
        self.setWindowTitle('Game of Life')
        self.show()

    def redraw(self, cells):
        print("draw")
        for x in range(self.w):
            for y in range(self.h):
                if cells[x][y]:
                    self.buttons[x][y].setStyleSheet("background-color: black")
                else:
                    self.buttons[x][y].setStyleSheet("background-color: white")
