from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell
from collections import namedtuple

# Using "# type: ignore" because VSCode doesn't like python 3.6.8 style list type hints

class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, prev, value=None, next=None):
        self.prev: ListNode = prev
        self.next: ListNode = next
        self.value = value
    
    def setNext(self, next):
        self.next = next
    
    def setPrev(self, prev):
        self.prev = prev
    
    def setValue(self, value):
        self.value = value
               
    
    # def walk(self, indent=0):
    #         if isinstance(self.value, ListNode):
    #             print("Value is node")
    #             self.value.walk(indent + 1)
    #         else:
    #             print(f'{"   "*indent}{self.value}')

    #         if self.next is not None:
    #             self.next.walk(indent)
    def walk(self, indent=0):
        if isinstance(self.value, dict):
            self.value['head'].walk(indent + 1)
            print()
        else:
            if self.value is None:
                print('_', end = ' ')
            else:
                print(self.value, end=' ')
    
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
        self.tail: ListNode = None

        self.numRows = 0
        self.numColumns = 0


    def buildSpreadsheet(self, lCells: [Cell]): # type: ignore
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        
        currRow: ListNode = None
        self.head = None
        
        self.numRows = max((cell.row for cell in lCells)) + 1
        self.numColumns = max((cell.col for cell in lCells)) + 1
        
        for i in range(self.numRows):
            # Create a new row node
            newRow = ListNode(currRow)
            if self.head is None:
                self.head = newRow
            else:
                currRow.setNext(newRow)
            currRow = newRow

            # Create all the cells in the row
            newRowHead, newRowTail = self._makeNewRow(self.numColumns)

            # Point the row node to the row head
            currRow.setValue({'head': newRowHead, 'tail': newRowTail})
        
        self.tail = currRow
        

        for cell in lCells:
            node = self._findByIndex(cell.row, cell.col)
            node.setValue(cell.val)
        

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """
        
        newTail = ListNode(self.tail)
        newTailHead, newTailTail = self._makeNewRow(self.numColumns)
        
        newTail.setValue({'head': newTailHead, 'tail': newTailTail})
        self.tail.setNext(newTail)
        self.tail = newTail
        self.numRows += 1


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        
        curr = self.head

        while curr is not None: # For each row
            newNode = ListNode(curr.value['tail'])
            
            curr.value['tail'].setNext(newNode)
            curr.value['tail'] = newNode
            
            curr = curr.next
        
        self.numColumns += 1
            
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        # Inserts after index
        
        if rowIndex < -1 or rowIndex >= self.numRows:
            return False
        
        if rowIndex == -1:
            newRowHead, newRowTail = self._makeNewRow(self.numColumns)
            
            newRow = ListNode(None, {'head': newRowHead, 'tail': newRowTail}, self.head)
            self.head.setPrev(newRow)
            self.head = newRow
        else:
            # Make new row
            newRowHead, newRowTail = self._makeNewRow(self.numColumns)

            # Find location to insert
            curr = self.head
            for i in range(rowIndex):
                curr = curr.next
           
            # Insert row
            newRow = ListNode(curr, {'head': newRowHead, 'tail': newRowTail}, curr.next)
            if curr.next is not None:
                curr.next.setPrev(newRow)
            curr.setNext(newRow)
        
        self.numRows += 1

        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """
        
        if colIndex < -1 or colIndex >= self.numColumns:
            return False


        curr = self.head
        while curr is not None: # For all rows
            if colIndex == -1:
                newNode = ListNode(None, next=curr.value['head'])
                curr.value['head'].setPrev(newNode)
                curr.value['head'] = newNode
            else:
                # Find where to insert
                currNode = curr.value['head']
                for i in range(colIndex):
                    currNode = currNode.next
                
                newNode = ListNode(currNode, next=currNode.next)
                if currNode.next is not None:
                    currNode.next.setPrev(newNode)
                currNode.setNext(newNode)

            curr = curr.next
        
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

        if rowIndex < 0 or rowIndex >= self.numRows or colIndex < 0 or colIndex >= self.numRows:
            return False

        node = self._findByIndex(rowIndex, colIndex)
        node.setValue(value)

        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        return self.colNum


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        return self.rowNum



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


    def _makeNewRow(self, length):
        curr = ListNode(None)
        head = curr
        
        for i in range(length - 1):
            newNode = ListNode(curr)
            curr.setNext(newNode)
            curr = newNode
        
        tail = curr
        
        return head, tail



    def print(self) -> None:
        self.head.walk()
    
    def _findByIndex(self, row: int, column: int) -> ListNode:
        curr = self.head
        for i in range(row):
            curr = curr.next
        
        curr = curr.value['head']
        for i in range(column):
            curr = curr.next
        
        return curr

        


def main():
    spreadsheet = LinkedListSpreadsheet()
    spreadsheet.buildSpreadsheet([Cell(0, 0, 1), Cell(1, 1, 2), Cell(2, 2, 3)])
    spreadsheet.print()
    
    print()
    spreadsheet.update(0, 1, 5)
    spreadsheet.print()

if __name__ == '__main__':
    main()