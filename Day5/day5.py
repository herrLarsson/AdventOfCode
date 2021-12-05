import csv
import numpy as np


def getInput(test):
    file='input.csv'
    if test==True:
        file='testInput.csv'
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[0]

def part1(test):
    data=getInput(test)
    board=generateBoard(test)
    for line in data:
        s=line.split()
        if isVerticalOrHorisontal(s[0],s[2])==True:
            markBoardHorisontal(s[0], s[2], board)
    return getIntersections(board, 2)

def part2(test):
    data=getInput(test)
    board=generateBoard(test)
    for line in data:
        s=line.split()
        if isVerticalOrHorisontal(s[0],s[2])==True:
            markBoardHorisontal(s[0], s[2], board)
        else:
            markBoardDiagonal(s[0], s[2], board)
    return getIntersections(board, 2)

def isVerticalOrHorisontal(x,y):
    xlist=x.split('.')
    ylist=y.split('.')
    return xlist[0]==ylist[0] or xlist[1]==ylist[1]

def markBoardHorisontal(x,y,board):
    
    xlist=x.split('.')
    ylist=y.split('.')
    x1=int(xlist[0])
    y1=int(xlist[1])
    x2=int(ylist[0])
    y2=int(ylist[1])
    if x1 > x2:
        tempx=x1
        x1=x2
        x2=tempx
    if y1 > y2:
        tempy=y1
        y1=y2
        y2=tempy
    if y1!=y2:
        for y in range(y1,y2+1):
            board[y][x1]+=1
    else :
        for x in range(x1,x2+1):
            board[y1][x]+=1
            
def markBoardDiagonal(x,y,board):
    
    list1=x.split('.')
    list2=y.split('.')
    x1=int(list1[0])
    y1=int(list1[1])
    x2=int(list2[0])
    y2=int(list2[1])
    x=x1
    y=y1
    xAsc=x1<x2
    yAsc=y1<y2
    if yAsc:
        y2+=1
    else:
        y2-=1
    if xAsc:
        x2+=1
    else:
        x2-=1
    while(y!=y2 and x!=x2):
        board[y][x]+=1
        if xAsc:
            x+=1
        else:
            x-=1
        if yAsc:
            y+=1
        else:
            y-=1

def getIntersections(board, value):
    count=0
    for line in board:
        for row in line:
            if int(row)>1:
                count+=1
    return count
    
def generateBoard(test):
    grid_size=1000
    if test==True:
        grid_size=10
    return np.zeros((grid_size,grid_size))

print(part1(False))
print(part2(False))

