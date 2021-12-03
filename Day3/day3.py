import csv

def getInput():
    with open('input.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[0]
    
def getMcb(index, lista):
    mcb = 0;
    for binary in lista:
        if int(binary[index]) > 0:
                mcb += 1
        else:
            mcb -= 1
    if mcb > 0:
        return 1
    elif mcb < 0:
        return 0
    else:
        return 2
    
def getLcb(index, lista):
    result = getMcb(index, lista)
    if result == 0:
        return 1
    elif result == 1:
        return 0
    return result

def getOxy(lista,index):
    if len(lista) == 1:
        return int(lista[0],2)
    else:
        reducedList = list()
        mcb = getMcb(index,lista)
        for item in lista:
            if (int(item[index]) == mcb) or (mcb == 2 and int(item[index]) == 1):
                reducedList.append(item)
        if index <= len(lista[0]):
            return getOxy(reducedList,index+1)
        
def getC02(lista,index):
    if len(lista) == 1:
        return int(lista[0],2)
    else:
        reducedList = list()
        lcb = getLcb(index,lista)
        for item in lista:
            if (int(item[index]) == lcb) or (lcb == 2 and int(item[index]) == 0):
                reducedList.append(item)
        if index <= len(lista[0]):
            return getC02(reducedList,index+1)
    
def getGammaRate(lista):
    gammaRate = ''
    for i in range(12):
        gammaRate += str(getMcb(i,lista))
    return int(gammaRate,2)

def getEpsilonRate(lista):
    epsilonRate = ''
    for i in range(12):
        epsilonRate += str(getLcb(i,lista))
    return int(epsilonRate,2)

def getPower(gammaRate, epsilonRate):
    return gammaRate * epsilonRate

def part1():
    data = getInput()
    return getPower(getGammaRate(data), getEpsilonRate(data))

def part2():
    data = getInput()
    return getC02(data,0) * getOxy(data,0)
            
            
print(part1())
print(part2())
