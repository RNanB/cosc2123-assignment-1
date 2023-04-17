from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------




class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.numRows = 0
        self.numColumns = 0
        
        self.colA: list = []
        self.valA: list = []
        self.sumA: list = [0]


    def buildSpreadsheet(self, lCells: list[Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        
        self.numRows = max((cell.row for cell in lCells)) + 1
        self.numColumns = max((cell.col for cell in lCells)) + 1
        
        currSum = 0

        for cell in lCells:
            self.valA.append(cell.val)
            self.colA.append(cell.col)
            
            # Update sumA
            if len(self.sumA) - 1 <= cell.row:
                self.sumA.append(self.sumA[-1] + cell.val)
            else:
                for i in range(cell.col + 1, len(self.sumA)):
                    self.sumA[i] += cell.val



        # TO BE IMPLEMENTED
        pass


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        self.numRows += 1
        self.sumA.append(self.sumA[-1])


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        pass


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True



    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return 0


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return 0




    def find(self, value: float) -> list[(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []




    def entries(self) -> list[Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """

        return []


    def debug(self) -> None:
        print(f'colA: {self.colA}')
        print(f'valA: {self.valA}')
        print(f'sumA: {self.sumA}')
        print(f'numRows: {self.numRows}')
        print(f'numColumns: {self.numColumns}')

    def toList(self) -> list[list]:
        # All zero list with the right size
        outputList = [[0 for i in range(self.numColumns)] for i in range(self.numRows)]

        row = 0
        sum = 0
        for i, currVal in enumerate(self.valA):
            column = self.colA[i]
            
            # If the sum matches, move on to the next row
            # What about when the row reaches its sum before the end, because of negatives?
            # Apparently we don't need to cover that case, according to Jeffrey Chan
            while sum == self.sumA[row + 1]:
                row += 1
            
            outputList[row][column] = currVal
            sum += currVal
        
        return outputList


def main():
    csr = CSRSpreadsheet()
    csr.buildSpreadsheet([Cell(0, 2, 3), Cell(1, 1, 4), Cell(2, 0, 6), Cell(2, 2, -2)])
    
    csr.debug()
    print(csr.toList())

if __name__ == '__main__':
    main()