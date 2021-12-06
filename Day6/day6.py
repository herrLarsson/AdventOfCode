import csv

def getInput(test):
    file='input.csv'
    if test==True:
        file='testInput.csv'
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[0]

def part1(test):
    data = getInput(test)
    return simulate(data, 80)

def part2(test):
    data = getInput(test)
    return simulate(data, 256)

def simulate(fishes, days):
    day = 0
    dayList = [0] * 9
    for fish in fishes:
        dayList[int(fish)] += 1
    while day < days:
        day += 1
        breeders = dayList.pop(0)
        dayList.append(breeders)
        dayList[6] += breeders
    return sum(dayList)

print( part1( False ))
print( part2( False ))
