def factors(x):
    fac = list()
    for i in range(1, x + 1):
        if x % i == 0:
            fac.append(i)
    return fac


def sum(l):
    c = 0
    for i in l:
        c += i
    return c


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def stickListAsString(l):
    s = ''
    for item in l:
        s = f'{s}{item}'
    return s


results = []
valid = True

while True:
    n, b = map(int, input().split())
    if n == -1 and b == -1:
        break

    if not (2 <= b <= 9):
        valid = False

    majmoo = sum(factors(n))
    results.append(int(stickListAsString(numberToBase(majmoo, b))))

if valid:
    print(sum(results))
else:
    print('invalid base!')
