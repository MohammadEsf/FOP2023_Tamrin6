firstNumber = int(input())
secondNumber = int(input())
constantNumber = int(input())


def add(firstNumber , secondNumber):
    while secondNumber != 0:
        sum = firstNumber ^ secondNumber

        carry = (firstNumber & secondNumber) << 1

        firstNumber = sum
        secondNumber = carry

    return firstNumber

majmoo = add(firstNumber , secondNumber)


def areEqual(sum , toCheck):
    if sum == toCheck:
        return 'YES'
    else:
        return 'NO'


result = areEqual(majmoo , constantNumber)

print(majmoo)
print(result)