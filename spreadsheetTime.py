import sys
from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.arraySpreadsheet import ArraySpreadsheet
from spreadsheet.linkedlistSpreadsheet import LinkedListSpreadsheet
from spreadsheet.csrSpreadsheet import CSRSpreadsheet
from timeit import timeit


# -------------------------------------------------------------------
# DON'T CHANGE THIS FILE.
# This is the entry point to run the program in file-based mode.
# It uses the data file to initialise the set of words & frequencies.
# It takes a command file as input and output into the output file.
# Refer to usage() for exact format of input expected to the program.
#
# __author__ = 'Jeffrey Chan, original file by Son Hoang Dau'
# __copyright__ = 'Copyright 2023, RMIT University'
# -------------------------------------------------------------------


def usage():
    """
    Print help/usage message.
    """

    # On Teaching servers, use 'python3'
    # On Windows, you may need to use 'python' instead of 'python3' to get this to work
    print('python3 spreadsheetFilebased.py', '<approach> <data fileName> <command fileName> <output fileName>')
    print('<approach> = <array | linkedlist | csr>')
    sys.exit(1)


if __name__ == '__main__':
    # Fetch the command line arguments
    args = sys.argv

    if len(args) != 5:
        print('Incorrect number of arguments.')
        usage()

    # initialise spreadsheet object
    spreadsheet: BaseSpreadsheet = None
    if args[1] == 'array':
        spreadsheet = ArraySpreadsheet()
    elif args[1] == 'linkedlist':
        spreadsheet = LinkedListSpreadsheet()
    elif args[1] == 'csr':
        spreadsheet = CSRSpreadsheet()
    else:
        print('Incorrect argument value.')
        usage()

    # read from data file to populate the initial set of points
    dataFilename = args[2]
    cellsFromFiles = []
    try:
        dataFile = open(dataFilename, 'r')
        for line in dataFile:
            values = line.split()
            currRow = int(values[0])
            currCol = int(values[1])
            currVal = float(values[2])
            currCell = Cell(currRow, currCol, currVal)
            # each line contains a cell
            cellsFromFiles.append(currCell)
        dataFile.close()
        # construct the spreadsheet from the read in data
        spreadsheet.buildSpreadsheet(cellsFromFiles)
    except FileNotFoundError as e:
        print("Data file doesn't exist.")
        usage()

    # filename of input commands
    commandFilename = args[3]
    # filename of output
    outputFilename = args[4]

    # Parse the commands in command file
    try:
        commandFile = open(commandFilename, 'r')
        outputFile = open(outputFilename, 'w')

        # for each command
        for line in commandFile:
            commandValues = line.split()
            command = commandValues[0]
            command = command.upper()
            # append row
            if command == 'AR':
                # result = spreadsheet.appendRow()
                # if result:
                #     outputFile.write("Call to appendRow() returned success.\n")
                # else:
                #     outputFile.write("Call to appendRow() returned failture.\n")
                
                time = timeit('spreadsheet.appendRow()', number=1, globals=globals())
                outputFile.write(f'appendRow() executed in {time*1000:.5f} ms\n')
            # append column
            elif command == 'AC':
                # result = spreadsheet.appendCol()
                # if result:
                #     outputFile.write("Call to appendCol() returned success.\n")
                # else:
                #     outputFile.write("Call to appendCol() returned failture.\n")
                
                time = timeit('spreadsheet.appendCol()', number=1, globals=globals())
                outputFile.write(f'appendCol() executed in {time*100:.5f} ms\n')
            # insert row
            elif command == 'IR':
                rowIndex = int(commandValues[1])
                # result = spreadsheet.insertRow(rowIndex)
                # if result:
                #     outputFile.write("Call to insertRow(" + str(rowIndex) + ") returned success.\n")
                # else:
                #     outputFile.write("Call to insertRow(" + str(rowIndex) + ") returned failure.\n")
                
                time = timeit('spreadsheet.insertRow(rowIndex)', number=1, globals=globals())
                outputFile.write(f'insertRow({rowIndex}) executed in {time*100:.5f} ms\n')
            # insert column
            elif command == 'IC':
                colIndex = int(commandValues[1])
                # result = spreadsheet.insertCol(colIndex);
                # if result:
                #     outputFile.write("Call to insertCol(" + str(colIndex) + ") returned success.\n")
                # else:
                #     outputFile.write("Call to insertCol(" + str(colIndex) + ") returned failure.\n")
                
                time = timeit('spreadsheet.insertCol(colIndex)', number=1, globals=globals())
                outputFile.write(f'insertCol({colIndex}) executed in {time*100:.5f} ms\n')
            # update value
            elif command == 'U':
                rowIndex = int(commandValues[1])
                colIndex = int(commandValues[2])
                value = float(commandValues[3])
                # result = spreadsheet.update(rowIndex, colIndex, value);
                # if result:
                #     outputFile.write("Call to update(" + str(rowIndex) + "," + str(colIndex) + "," + str(value) + ") returned success.\n")
                # else:
                #     outputFile.write("Call to update(" + str(rowIndex) + "," + str(colIndex) + "," + str(value) + ") returned failure.\n")
                
                time = timeit('spreadsheet.update(rowIndex, colIndex, value)', number=1, globals=globals())
                outputFile.write(f'update({rowIndex}, {colIndex}, {value}) executed in {time*100:.5f} ms\n')
            # number of rows
            elif command == 'R':
                # result = spreadsheet.rowNum();
                # outputFile.write("Number of rows = " + str(result) + "\n")

                time = timeit('spreadsheet.rowNum()', number=1, globals=globals())
                outputFile.write(f'rowNum() executed in {time*100:.5f} ms\n')
            # number of columns
            elif command == 'C':
                # result = spreadsheet.colNum();
                # outputFile.write("Number of columns = " + str(result) + "\n")

                time = timeit('spreadsheet.colNum()', number=1, globals=globals())
                outputFile.write(f'colNum() executed in {time*100:.5f} ms\n')
            # find value
            elif command == 'F':
                value = float(commandValues[1])
                # lCells = spreadsheet.find(value);
                # outputFile.write("Printing output of find(" + str(value) + "): ")
                # outputFile.write(" | ".join(["".join(["(", str(cell[0]), ",", str(cell[1]), ")"]) for cell in lCells]))
                # outputFile.write("\n")

                time = timeit('spreadsheet.find(value)', number=1, globals=globals())
                outputFile.write(f'find({value}) executed in {time*100:.5f} ms\n')
            # enumerate all entries that has a value in spreadsheet
            elif command == 'E':
                # lCells = spreadsheet.entries();
                # outputFile.write("Printing output of entries(): ")
                # outputFile.write(" | ".join([cell.__str__() for cell in lCells]))
                # outputFile.write("\n")

                time = timeit('spreadsheet.entries()', number=1, globals=globals())
                outputFile.write(f'entries() executed in {time*100:.5f} ms\n')
            else:
                print('Unknown command.')
                print(line)

        outputFile.close()
        commandFile.close()
    except FileNotFoundError as e:
        print("Command file doesn't exist.")
        usage()
