from datetime import datetime
from spreadsheet import Spreadsheet
from cell import Cell
from color import Color


class CellTests:
    def test_set_value(self):
        cell = Cell(value=20)
        value = cell.get_value()
        return value == "20"

    def test_get_value(self):
        cell = Cell(value=20)
        return cell.get_value() == "20"

    def test_set_color(self):
        cell = Cell()
        cell.set_color(Color.GREEN)
        return cell.color == Color.GREEN

    def test_get_color(self):
        cell = Cell(color=Color.RED)
        return cell.get_color() == Color.RED

    def test_to_int(self):
        cell = Cell(value="12")
        return cell.to_int() == 12

    def test_to_float(self):
        cell = Cell(value="12")
        return cell.to_float() == 12.0

    def test_to_date(self):
        cell = Cell(value="12-01-2022")
        return (isinstance(cell.to_date(), datetime)) or cell.to_date() == f"Cannot convert {cell} to date"

    def test_reset(self):
        cell = Cell()
        cell.set_color(Color.GREEN)
        cell.set_value("2022-02-02")
        cell.reset()
        return (cell.value == "") and (cell.color == Color.WHITE)


class Spreadsheet_Tests:

    def test_set_cell_at(self):
        spreadsheet.set_cell_at(1, 1, cell)
        res = spreadsheet.get_cell_at(2, 2)
        return res == cell


    def test_get_cell_at(self):
        spreadsheet.set_cell_at(1, 1, cell)
        res = spreadsheet.get_cell_at(2, 2)
        return res == cell

    def test_add_row(self):
        spreadsheet.set_cell_at(1, 1, cell)
        spreadsheet.add_row(0)
        return (spreadsheet.rows == 4) and (spreadsheet.sheet[2][1].value == "Hello")

    def test_remove_row(self):
        spreadsheet.set_cell_at(1, 1, cell)
        spreadsheet.add_row(0)
        spreadsheet.remove_row(1)
        return (spreadsheet.rows == 3) and (spreadsheet.sheet[0][0].value == "Hello")

    def test_add_col(self):
        spreadsheet.set_cell_at(1, 1, cell)
        spreadsheet.add_column(0)
        return (spreadsheet.columns == 4) and (spreadsheet.sheet[1][2].value == "Hello")

    def test_remove_col(self):
        spreadsheet = Spreadsheet(2, 2)
        cell = Cell(value="Hello", color=Color.RED)
        spreadsheet.set_cell_at(1, 1, cell)
        spreadsheet.add_column(0)
        spreadsheet.remove_column(1)
        return (spreadsheet.columns == 2) and (spreadsheet.sheet[1][1].value == "Hello")

    def test_swap_rows(self):
        spreadsheet.set_cell_at(1, 1, cell)
        spreadsheet.swap_rows(1, 2)
        return spreadsheet.sheet[0][1].value == "Hello"

    def test_swap_col(self):
        spreadsheet.set_cell_at(2, 1, cell)
        spreadsheet.swap_columns(1, 2)
        return spreadsheet.sheet[2][2].value == "Hello"




cell_tests = CellTests()
spreadsheet = Spreadsheet(3, 3)
cell = Cell(value="Hello", color=Color.RED)

cell_tests = [
    ("set_value", CellTests().test_set_value),
    ("get_value", CellTests().test_get_value),
    ("set_color", CellTests().test_set_color),
    ("get_color", CellTests().test_get_color),
    ("to_int", CellTests().test_to_int),
    ("to_float", CellTests().test_to_float),
    ("to_date", CellTests().test_to_date),
    ("reset", CellTests().test_reset)
]

for test in cell_tests:
    if test[1]():
        print(f"{test[0]} Passed")
    else:
        print(f"{test[0]} Failed")


spreadsheet_tests = Spreadsheet_Tests()
tests = [spreadsheet_tests.test_set_cell_at,
         spreadsheet_tests.test_get_cell_at,
         spreadsheet_tests.test_add_row,
         spreadsheet_tests.test_remove_row,
         spreadsheet_tests.test_add_col,
         spreadsheet_tests.test_remove_col,
         spreadsheet_tests.test_swap_rows,
         spreadsheet_tests.test_swap_col]
for test in tests:
    if test():
        print(f"{test.__name__} Passed")
    else:
        print(f"{test.__name__} Failed")
