class Cells:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[False for j in range(w)] for i in range(h)]

    def set_cell(self, x, y):
        self.cells[x][y] = True

    def get_next_condition(self, x, y):
        # TODO: implement game of life rules
        return False

    def get_next(self):
        # get new condition for all cells
        new_cells = self.cells
        for y in self.cells:
            for x in row:
                new_cells[x][y] = self.get_next_condition(x, y)
        return new_cells
