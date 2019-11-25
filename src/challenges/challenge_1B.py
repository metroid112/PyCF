"""
In the popular spreadsheets systems (for example, in Excel) the following numeration of columns is used.
The first column has number A, the second — number B, etc. till column 26 that is marked by Z. Then there
are two-letter numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ. After ZZ there
follow three-letter numbers, etc.

The rows are marked by integer numbers starting with 1. The cell name is the concatenation of the column
and the row numbers. For example, BC23 is the name for the cell that is in column 55, row 23.

Sometimes another numeration system is used: RXCY, where X and Y are integer numbers, showing the column
and the row numbers respectfully. For instance, R23C55 is the cell from the previous example.

Your task is to write a program that reads the given sequence of cell coordinates and produce each item
written according to the rules of another numeration system.

Input
The first line of the input contains integer number n (1 ≤ n ≤ 105), the number of coordinates in the test.
Then there follow n lines, each of them contains coordinates. All the coordinates are correct, there are
no cells with the column and/or the row numbers larger than 106 .

Output
Write n lines, each line should contain a cell coordinates in the other numeration system.

Examples
input
    2
    R23C55
    BC23
output
    BC23
    R23C55
"""


def challenge(args):
    coords = args[1:]
    for coord in coords:
        if coord[0] == 'R':
            row = coord[1:].split('C')[0]
        else:
            i = 1
            row = ''
            while row == '' or row == coord:
                row = coord.split(str(i))[0]
                i += 1
            print(list(map(lambda x: x * 2, row)))
        print(row, coord)
