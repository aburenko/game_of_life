from PyQt5.QtWidgets import (QWidget, QCheckBox)
import threading
import time


# TODO add stop button and speed regulation
class Game(QWidget):

    def __init__(self, w, h, cells, timer):
        # init vars
        self.w = w
        self.h = h
        self.boxes = [[None for j in range(self.w)] for i in range(self.h)]
        self.cells = cells
        # init ui
        super().__init__()
        self.init_ui()
        # start polling with new thread
        t = threading.Thread(target=self.get_next, args=(timer,))
        t.start()

    def get_next(self, timer):
        while True:
            # load new cells and redraw
            cells_new = self.cells.get_next()
            self.redraw(cells_new)
            # self.update()
            time.sleep(timer)

    def button_clicked(self):
        sender = self.sender()
        # get x,y values of button and send to Cells
        tip = sender.toolTip()
        x, y = tip.split(':')
        self.cells.set_cell(int(x), int(y))

    def init_ui(self):
        margin = 20
        # create buttons to simulate cells
        for x in range(self.w):
            for y in range(self.h):
                check_box = QCheckBox('', self)
                check_box.setToolTip(str(x) + ":" + str(y))
                check_box.move(x * margin, y * margin)
                check_box.resize(margin, margin)
                check_box.setStyleSheet("QCheckBox::indicator:unchecked {image: url(./images/unchecked.bmp);}"
                                        "QCheckBox::indicator:checked {image: url(./images/checked.bmp);}"
                                        "QCheckBox::indicator:checked:hover {image: url(./images/pressed.bmp);}"
                                        )
                check_box.pressed.connect(self.button_clicked)
                # noinspection PyTypeChecker
                self.boxes[x][y] = check_box
        # set window
        self.setGeometry(margin * self.w, margin * self.h, margin * self.w, margin * self.h)
        self.setWindowTitle('Game of Life')
        self.show()

    def redraw(self, cells):
        # redraw buttons
        for x in range(self.w):
            for y in range(self.h):
                if cells[x][y]:
                    self.boxes[x][y].setChecked(True)
                else:
                    self.boxes[x][y].setChecked(False)
