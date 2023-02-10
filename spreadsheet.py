from cell import Cell


class Spreadsheet:
    def __init__(self, rows=0, columns=0):
        if rows <= 0 or columns <= 0:
            raise ValueError("Number of row or columns must be positive!")
        self.rows = rows
        self.columns = columns
        self.sheet = [[Cell() for i in range(columns)]for j in range(rows)]

    def set_cell_at(self, row, column, cell):
        if row > 0 and (row <= self.rows) and (column > 0) and (column <= self.columns):
            self.sheet[row][column] = cell

    def get_cell_at(self, row, column):
        if row > 0 and (row <= self.rows) and (column > 0) and (column <= self.columns):
            return self.sheet[row-1][column-1]

    def add_row(self, row):
        if row >= 0 and (row <= self.rows):
            self.rows += 1
            self.sheet.insert(row+1, [Cell() for j in range(self.columns)])

    def remove_row(self, row):
        if row >= 0 and row < self.rows:
            self.rows -= 1
            self.sheet.pop(row)

    def add_column(self, column):
        if (column >= 0) and (column < self.columns):
            self.columns += 1
            for i in range(self.rows):
                self.sheet[i].insert(column, Cell())

    def remove_column(self, column):
         if column > 0 and (column <= self.columns):
            self.columns -= 1
            for i in range(self.rows):
                self.sheet[i].pop(column - 1)

    def swap_rows(self, row1, row2):
        if row1 > 0 and (row2 > 0) and (row1 <= self.rows) and (row2 <= self.rows):
            if row1 != row2:
                for i in range(self.columns):
                    tmp = self.sheet[row1-1][i]
                    self.sheet[row1-1][i] = self.sheet[row2-1][i]
                    self.sheet[row2-1][i] = tmp
            else:
                return
        else:
            raise IndexError("Invalid Row Number")


    def swap_columns(self, col1, col2):
        if col1 > 0 and (col1 <= self.columns) and (col2 > 0) and (col2 <= self.columns):
            if col1 != col2:
                for i in range(self.rows):
                    tmp = self.sheet[i][col1]
                    self.sheet[i][col1] = self.sheet[i][col2]
                    self.sheet[i][col2] = tmp
            else:
                return
        else:
            raise IndexError("Invalid Column Number")

