import csv
import math

with open('data.csv',newline='') as dataone:
    reader1 = csv.reader(dataone)
    file_data = list(reader1.read())

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    
    mean = total / n
    return mean

squared_list = []
for number in data:
    a = int(number) - mean(data)
    a =a**2
    squared_list.append(a)

    sum = 0
    for i in squared_list:
        sum = sum+1

    result = sum/(len(data)-1)

    std_deviation = math.sqrt(result)
    print(std_deviation)



