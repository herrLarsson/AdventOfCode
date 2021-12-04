import csv

def getInput():
    with open('input.csv', newline = '') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[0]
    
def getBingoBoards():
    with open('boards.csv', newline = '') as f:
        reader = csv.reader(f)
        data = list(reader)
        boardList = list()
        board = list()
        for line in data[0]:
            if len(line) != 0:
                if len(board) < 5:
                    board.append(line.split())
                else:
                    boardList.append(board)
                    board = list()
                    board.append(line.split())
        return boardList
    
def markBoard(boards, drawnNumber):
    for board in boards:
        for line in board:
            for number in range(len(line)):
                if(line[number] != "X" and int(line[number]) == int(drawnNumber)):
                    line[number] = "X"
def checkBoard(boards):
    vertical_X = 0
    horisontal_X = 0
    for board in boards:
        for line in board:
            for number in line:
                if number == "X":
                    horisontal_X += 1
            if horisontal_X == 5:
                #Bingo
                return board
            else:
                horisontal_X = 0
        for x in range(5):
            for y in range(5):
                if board[y][x] == "X":
                    vertical_X += 1
            if vertical_X == 5:
                #Bingo
                return board
            else:
                vertical_X = 0
def checkAndSaveBoard(boards):
    vertical_X = 0
    winlist = list()
    horisontal_X = 0
    for board in boards:
        for line in board:
            for number in line:
                if number == "X":
                    horisontal_X += 1
            if horisontal_X == 5:
                #Bingo
                winlist.append(board)
            else:
                horisontal_X = 0
        for x in range(5):
            for y in range(5):
                if board[y][x] == "X":
                    vertical_X += 1
            if vertical_X == 5:
                #Bingo
                winlist.append(board)
            else:
                vertical_X = 0
    return winlist

def getSum(board):
    summa = 0
    for line in board[0]:
        for number in line:
            if number != "X":
                summa += int(number)
    return (summa * int(board[1]))

def part1():
    boards = getBingoBoards()
    rad = getInput()
    for value in rad:
        markBoard(boards,value)
        result = checkBoard(boards)
        if result != None:
            return getSum([result, value])

def part2():
    boards = getBingoBoards()
    winList = list()
    rad = getInput()
    for value in rad:
        markBoard(boards,value)
        result = checkAndSaveBoard(boards)
        if len(result) > 0:
            for l in result:
                try:
                    winList.append([l, value])
                    boards.remove(l)
                except ValueError:
                    #could not remove board from list because it is a duplicate
                    winList.remove([l, value])
                    pass
                
    return getSum(winList[-1])

print(part1())  
print(part2())
    
