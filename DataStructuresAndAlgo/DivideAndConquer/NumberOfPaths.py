def numberOfPaths(twoDArray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numberOfPaths(twoDArray, 0, col-1, cost-twoDArray[row][col])
    elif col == 0:
        return numberOfPaths(twoDArray, row-1, 0, cost-twoDArray[row][col])
    else:
        opt1 = numberOfPaths(twoDArray, row - 1, col, cost-twoDArray[row][col])
        opt2 = numberOfPaths(twoDArray, row, col - 1, cost-twoDArray[row][col])
        return opt1 + opt2

twoDList = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 6, 2],
    [7, 1, 7 ,3],
]

print(numberOfPaths(twoDList, 3, 3, 25))