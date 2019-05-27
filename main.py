import sys
from PyQt5.QtWidgets import (QApplication)
# import gui and cells class
import gui
import cells


if __name__ == '__main__':
    # set number of cells
    width = 20
    height = 20
    timer = 1
    # init cells
    cells = cells.Cells(width, height)
    # init gui
    app = QApplication(sys.argv)
    app.setStyle('cleanlooks')
    ex = gui.Game(width, height, cells, timer)
    sys.exit(app.exec_())
