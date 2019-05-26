import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)


class Game(QWidget):

    def __init__(self):
        self.w = 20
        self.h = 20
        self.buttons = [[None for j in range(self.w)] for i in range(self.h)]

        super().__init__()
        self.init_ui()

    def button_clicked(self):
        sender = self.sender()
        sender.setStyleSheet("background-color: yellow")

    def init_ui(self):
        for x in range(self.w):
            for y in range(self.h):
                btn = QPushButton('', self)
                btn.move(x*20, y*20)
                btn.resize(20, 20)
                btn.clicked.connect(self.button_clicked)
                self.buttons[x][y] = btn

        self.setGeometry(300, 300, 20*self.w, 20*self.h)
        self.setWindowTitle('Game of Life')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec_())