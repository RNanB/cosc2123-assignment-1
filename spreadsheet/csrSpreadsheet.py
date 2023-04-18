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


    def buildSpreadsheet(self, lCells: list[Cell]) -> None:
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        
        self.numRows = max((cell.row for cell in lCells)) + 1
        self.numColumns = max((cell.col for cell in lCells)) + 1
        
        # Sort in order of what order they'll be in valA
        lCells.sort(key = lambda x: x.row * self.numColumns + self.numColumns)
        
        currSum = 0

        for cell in lCells:
            self.valA.append(cell.val)
            self.colA.append(cell.col)
            
            # First create sumA entries
            for i in range(len(self.sumA) - 1, cell.row + 1):
                self.sumA.append(self.sumA[-1])

            # Then add this cell to all applicable sumA entries
            for i in range(cell.row + 1, len(self.sumA)):
                self.sumA[i] += cell.val



        # TO BE IMPLEMENTED
        pass


    def appendRow(self) -> bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        self.numRows += 1
        self.sumA.append(self.sumA[-1])
        
        return True


    def appendCol(self) -> bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        self.numColumns += 1
        
        return True

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        
        # Description is confusing, do I do it after or before index?
        # I'm going to do it after because that's what the document says
        
        if rowIndex < -1 or rowIndex >= self.numRows:
            return False
        
        self.numRows += 1
        self.sumA.insert(rowIndex + 2, self.sumA[rowIndex + 1])

        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        
        # Inserts *after* index

        if colIndex < -1 or colIndex >= self.numColumns:
            return False
        
        for i , column in enumerate(self.colA):
            if column > colIndex:
                self.colA[i] += 1
        
        self.numColumns += 1

        return True



    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        
        if rowIndex >= self.numRows or colIndex >= self.numColumns or rowIndex < 0 or colIndex < 0:
            return False

        # First find index of valA to insert it in
        replace = False
        index: int = None

        row = 0
        sum = 0
        for i, currVal in enumerate(self.valA):
            column = self.colA[i]
            
            while sum == self.sumA[row + 1]:
                row += 1
            
            # Got to the coordinates, and there is no value there
            if row > rowIndex or (row == rowIndex and column > colIndex):
                index = i
                break

            # Got to the coordinates, but there is already a value there
            if row == rowIndex and column == colIndex:
                index = i
                replace = True
                break
            
            sum += currVal
        
        
        # If it got to the end without finding something, that means we're appending it at the end
        index = len(self.valA)

        
        if not replace:
            self.valA.insert(index, value)
            self.colA.insert(index, colIndex)
            for i in range(rowIndex + 1, self.numRows + 1):
                self.sumA[i] += value
        else:
            prevValue = self.valA[index]
            self.valA[index] = value
            for i in range(rowIndex + 1, self.numRows + 1):
                self.sumA[i] += value - prevValue
 
        

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        return self.numRows


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        return self.numColumns




    def find(self, value: float) -> list[(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        result: list[tuple[int, int]] = []

        row = 0
        sum = 0
        for i, currVal in enumerate(self.valA):
            column = self.colA[i]
            
            while sum == self.sumA[row + 1]:
                row += 1
            
            if currVal == value:
                result.append((row, column))

            sum += currVal


        # REPLACE WITH APPROPRIATE RETURN VALUE
        return result




    def entries(self) -> list[Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        
        result: list[Cell] = []

        row = 0
        sum = 0
        for i, currVal in enumerate(self.valA):
            column = self.colA[i]
            
            # If the sum matches, move on to the next row
            # What about when the row reaches its sum before the end, because of negatives?
            # Apparently we don't need to cover that case, according to Jeffrey Chan
            while sum == self.sumA[row + 1]:
                row += 1
            
            result.append(Cell(row, column, currVal))
            sum += currVal


        return result


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
    csr.buildSpreadsheet([
        Cell(9, 9, 2.0),
        Cell(2, 5, 7),
        Cell(3, 1, 6),
        Cell(8, 5, -6.7)
    ])

    csr.debug()
    
    csr.appendRow()
    csr.appendCol()
    
    csr.debug()
    csr.update(10, 10, 1.0)
    print(csr.toList())
    
if __name__ == '__main__':
    main()