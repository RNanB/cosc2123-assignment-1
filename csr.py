class CSR:
    def __init__(self, inputList: list[tuple]):
        self.numRows = len(inputList)
        self.numColumns = len(inputList[0])

        self.colA = []
        self.valA = []
        self.sumA = [0]
        
        currSum = 0

        for rowIndex, row in enumerate(inputList):
            for columnIndex, cell in enumerate(row):
                if cell == 0:
                    continue
                
                self.valA.append(cell)
                self.colA.append(columnIndex)
                currSum += cell
            
            self.sumA.append(currSum)
    
    
    def appendRowBottom(self, inputList: list) -> None:
        self.numRows += 1

        sum = self.sumA[-1]

        for column, cell in enumerate(inputList):
            if cell == 0:
                continue
            
            self.valA.append(cell)
            self.colA.append(column)
            sum += cell
        self.sumA.append(sum)
    
    
    def debug(self) -> None:
        print(f'colA: {self.colA}')
        print(f'valA: {self.valA}')
        print(f'sumA: {self.sumA}')
    
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
    test = [(0, 0, 3),
            (0, 4, 0),
            (6, 0, -2)
    ]
    
    csr = CSR(test)
    csr.appendRowBottom([1, 4, 0])
    csr.debug()
    print(csr.toList())


if __name__ == '__main__':
    main()