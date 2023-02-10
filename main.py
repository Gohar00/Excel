from color import Color
from cell import Cell
from spreadsheet import Spreadsheet


def show():
    # loop through all the rows and columns of the sheet
    for i in range(1, sheet.rows+1):
        for j in range(1, sheet.columns+1):
            # get the cell
            cell = sheet.get_cell_at(i, j)
            if cell:
                # print the value of the cell
                print(cell.get_value(), end="\t")
        print("\n")


sheet = Spreadsheet(3, 3)
cell = Cell(value="Hello", color=Color.RED)
show()
