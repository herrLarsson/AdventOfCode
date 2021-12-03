import csv

def getInput():
    with open('input.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[0]
    
def part1():
    data = getInput()
    horisontal_position = 0
    vertical_position = 0
    for x in data:
        cmdValue = x.split(' ')
        cmd = cmdValue[0]
        value = int(cmdValue[1])
        if (cmd =='forward'):
            horisontal_position += value
        elif (cmd == 'up'):
            vertical_position -= value
        elif (cmd == 'down'):
             vertical_position += value
             
    return horisontal_position * vertical_position

def part2():
    data = getInput()
    horisontal_position = 0
    vertical_position = 0
    aim = 0
    for x in data:
        cmdValue = x.split(' ')
        cmd = cmdValue[0]
        value = int(cmdValue[1])
        if (cmd == 'forward'):
            horisontal_position += value
            vertical_position += (aim * value)
        elif (cmd == 'up'):
            aim -= value
        elif (cmd == 'down'):
            aim += value
            
    return horisontal_position * vertical_position;

print(part1())
print(part2())
