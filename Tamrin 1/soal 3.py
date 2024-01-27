number1 = int(input())
number2 = int(input())
a = (bin(number1)[2:])
b = (bin(number2)[2:])

difference1 = (32 - len(a))
number1 = (difference1 * '0' + a )

difference2 = (32 - len(b))
number2 = (difference2 * '0' + b)

fullnumber = number2 + number1

n = int(input())
count = 0
list = []
while count != n:
    entry = int(input())
    list.append(entry)
    count = count + 1

for i in list:
    w = 63 - i
    if fullnumber[w] == '1':
        print('yes')
    else:
        print('no')