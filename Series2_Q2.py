import math
from functools import reduce


def lcd(a, b):
    return (a * b) // math.gcd(a, b)


listOfCommands = {'lcd', 'max', 'min', 'average', 'sum', 'gcd'}
tale = input()
if not(tale in listOfCommands):
    print('Invalid command')
    exit()

inputs = []
while True:
    vorodi = input()
    if vorodi == 'end':
        break
    vorodi = int(vorodi)
    inputs.append(vorodi)

# print(inputs)
if tale == 'sum':
    print(sum(inputs))
#
elif tale == 'average':
    miangin = sum(inputs) / len(inputs)
    print(round(miangin , 2))
#

elif tale == 'lcd':
    result = reduce(lcd, inputs)
    print(result)


elif tale == 'gcd':
    result = reduce(math.gcd, inputs)
    print(result)


elif tale == 'min':
    print(min(inputs))

elif tale == 'max':
    print(max(inputs))
