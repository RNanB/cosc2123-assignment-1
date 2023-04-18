from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jerome Peter Awad'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.array = []

    def buildSpreadsheet(self, lCells: [Cell]):
        n_row = max((cell.row for cell in lCells))
        n_col = max((cell.col for cell in lCells))

        self.array = [[None] * (n_col + 1) for _ in range(n_row + 1)]

        for cell in lCells:
            self.array[cell.row][cell.col] = cell.val

    def appendRow(self) -> bool:
        self.array.append([None] * self.colNum())
        return True

    def appendCol(self) -> bool:
        for row in self.array:
            row.append(None)
        return True

    def insertRow(self, rowIndex: int) -> bool:
        if rowIndex > self.rowNum() or rowIndex < 0:
            return False

        self.array.insert(rowIndex, [None] * self.colNum())
        return True

    def insertCol(self, colIndex: int) -> bool:
        if colIndex > self.colNum() or colIndex < 0:
            return False

        for row in self.array:
            row.insert(colIndex, None)

        return True

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        if rowIndex < 0 or rowIndex >= self.rowNum() or colIndex < 0 or colIndex >= self.colNum():
            return False

        self.array[rowIndex][colIndex] = value
        return True

    def rowNum(self) -> int:
        return len(self.array)

    def colNum(self) -> int:
        return len(self.array[0]) if self.array else 0

    def find(self, value: float) -> [(int, int)]:
        location = []
        for row_num, row in enumerate(self.array):
            for col_num, val in enumerate(row):
                if val == value:
                    location.append((row_num, col_num))

        return location

    def entries(self) -> [Cell]:
        entries = []
        for row_num, row in enumerate(self.array):
            for col_num, value in enumerate(row):
                if value is not None:
                    entries.append(Cell(row_num, col_num, value))

        return entries
