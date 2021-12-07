import csv
import numpy as np

def getInput(test):
    file='input.csv'
    if test==True:
        file='testInput.csv'
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return transformToInt(data[0])
    
def transformToInt(data):
    intList=list()
    for item in data:
        intList.append(int(item))
    return intList

def getMedian(data):
    return np.median(data)

def calcFuelCost(data, position):
    cost=0
    for item in data:
        if item >= position:
            cost += item-position
        else:
            cost += position-item
    return cost

def calcFuelCost2(data, position):
    cost=0
    for item in data:
        if item >= position:
            for i in range((item-int(position))+1):
                cost+=i
        else:
            for i in range((int(position)-item)+1):
                cost+=i
    return cost

def getCheapest(data):
    maxnum=np.amax(data)
    print(maxnum)
    cheapest=[0,0]
    for i in range(maxnum):
        result = calcFuelCost2(data, i)
        if(result<cheapest[0] or cheapest[0]==0):
            cheapest[0]=result
            cheapest[1]=i
    return cheapest
            
def part1(test):
    data=getInput(test)
    position = getMedian(data)
    return calcFuelCost(data,position)

def part2(test):
    data=getInput(test)
    return getCheapest(data)


print(part1(True))
print(part2(True))
