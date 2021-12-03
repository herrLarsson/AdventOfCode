import csv

def getInput():
    with open('input.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[0]
    
def part1():
    data = getInput()
    prevval = 999999
    summa = 0
    for line in data:
        for x in line:
            if (x! = ''):
                if (int(x) > prevval):
                    summa += 1
                prevval = int(x)
            return summa

def part2():
    data = getInput()
    prevval = 999999
    current = 0
    summa = 0
    for line in data:
        for x in range(len(line)-3):
            if ( x!= ''):
                temp = line[x:x+3]
                current = int(temp[0]) + int(temp[1]) + int(temp[2])
                print(current)
                if (current > prevval):
                    summa += 1
                prevval = current
                current = 0
        return summa
    
print(part1())
print(part2())
