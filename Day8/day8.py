import csv
import numpy as np

actual_value ={'abcdefg': 8,
 'abcdfg': 9,
 'abcefg': 0,
 'abdefg': 6,
 'abdfg': 5,
 'acdeg': 2,
 'acdfg': 3,
 'acf': 7,
 'bcdf': 4,
 'cf': 1}

def getInput(test):
    file='input.csv'
    if test==True:
        file='testInput.csv'
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data[0]
    

def part2(test):
    data=getInput(test)
    return decode2(data)
    

def part1(test):
    data=getInput(test)
    return decode(data)

def decode(data):
    counter=0
    for line in data:
        s=line.split("|")
        signalPattern=s[0].split()
        signalValue=s[1].split()
        numberSetList=list([set()]*9)
        
    
        for word in signalPattern:
            if len(word)==2 and not numberSetList[0]:
                numberSetList[0]=set(list(word))
            elif len(word)==3 and not numberSetList[6]:
                numberSetList[6]=set(list(word))
            elif len(word)==4 and not numberSetList[3]:
                numberSetList[3]=set(list(word))
            elif len(word)==7 and not numberSetList[7]:
                numberSetList[7]=set(list(word))
            if(numberSetList[0] and numberSetList[3] and numberSetList[6] and numberSetList[7]):
                break
            
        for word in signalValue:
            wordSet=set(list(word))
            if wordSet==numberSetList[0] or wordSet==numberSetList[3] or wordSet==numberSetList[6] or wordSet==numberSetList[7]:
                counter+=1
    return counter

def decode2(data):
    counter=0
    for line in data:
        s=line.split("|")
        signalPattern=s[0].split()
        signalValue=s[1].split()
        numberSetList=list([set()]*9)
        
        for word in signalPattern:
            wordSet=set(list(word))
            if len(word)==2 and not numberSetList[0]:
                numberSetList[0]=wordSet
            elif len(word)==3 and not numberSetList[6]:
                numberSetList[6]=wordSet
            elif len(word)==4 and not numberSetList[3]:
                numberSetList[3]=wordSet
            elif len(word)==7 and not numberSetList[7]:
                numberSetList[7]=wordSet
            if(numberSetList[0] and numberSetList[3] and numberSetList[6] and numberSetList[7]):
                break
            
        for number in signalPattern:
            number=set(list(number))
            if len(number) == 5 and len(numberSetList[0] & number) == 2:
                numberSetList[2]=number
            elif len(number) == 5 and len(numberSetList[3] & number) == 3:
                numberSetList[4]=number
            elif len(number) == 5:
                numberSetList[1]=number
            elif len(number) == 6 and len(numberSetList[3] & number) == 4:
                numberSetList[8]=number
            elif len(number) == 6 and len(numberSetList[6] & number) == 2:
                numberSetList[5]=number
        number=""
        for word in signalValue:
            wordSet=set(list(word))
            if wordSet==numberSetList[0]:
                number+="1"
            elif wordSet==numberSetList[4]:
                number+="5"
            elif wordSet==numberSetList[2]:
                number+="3"
            elif wordSet==numberSetList[1]:
                number+="2"
            elif wordSet==numberSetList[3]:
                number+="4"
            elif wordSet==numberSetList[5]:
                number+="6"
            elif wordSet==numberSetList[6]:
                number+="7"
            elif wordSet==numberSetList[7]:
                number+="8"
            elif wordSet==numberSetList[8]:
                number+="9"
            else: 
                number+="0"

        counter+=int(number)

               
                
    return counter
            

print(part1(False))
print(part2(False))
