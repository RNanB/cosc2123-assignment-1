from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

# Using "# type: ignore" because VSCode doesn't like python 3.6.8 style list type hints

class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, prev, value=None):
        self.prev: ListNode = prev
        self.next: ListNode = None
        self.value = value
    
    def setNext(self, next):
        self.next = next
    
    def setValue(self, value):
        self.value = value
    
    def findNode(self, row, column):
        pass

    def walk(self, indent=0):
            if isinstance(self.value, ListNode):
                print("Value is node")
                self.value.walk(indent + 1)
            else:
                print(f'{"   "*indent}{self.value}')

            if self.next is not None:
                self.next.walk(indent)

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.head: ListNode = None


    def buildSpreadsheet(self, lCells: [Cell]): # type: ignore
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        
        currRow: ListNode = None
        head = None
        
        numRows = max((cell.row for cell in lCells))
        numColumns = max((cell.col for cell in lCells))
        
        for i in range(numRows):
            # Create a new row node
            newRow = ListNode(currRow)
            if head is None:
                head = newRow
            else:
                currRow.setNext(newRow)
            currRow = newRow

            # Create all the cells in the row
            currCell = ListNode(None)
            newRowHead = currCell

            for j in range(numColumns - 1):
                newCell = ListNode(currCell)
                currCell.setNext(newCell)
                currCell = newCell

            # Point the row node to the row head
            currRow.setValue(newRowHead)
        
        tail = currRow
        
        

        # TO BE IMPLEMENTED
        pass


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """

        # TO BE IMPLEMENTED
        pass


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

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        # TO BE IMPLEMENTED
        pass

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
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        pass

        # TO BE IMPLEMENTED
        return 0


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        pass

        # TO BE IMPLEMENTED
        return 0



    def find(self, value: float) -> [(int, int)]: # type: ignore
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []



    def entries(self) -> [Cell]: # type: ignore
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # TO BE IMPLEMENTED
        pass

        # TO BE IMPLEMENTED
        return []


def main():
    spreadsheet = LinkedListSpreadsheet()
    spreadsheet.buildSpreadsheet([Cell(0, 0, 1), Cell(1, 1, 1), Cell(2, 2, 1)])

if __name__ == '__main__':
    main()