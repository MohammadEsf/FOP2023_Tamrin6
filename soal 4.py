avali, akhari = map(int, input().split())


def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def maximum(a, b):
    if a > b:
        return a
    else:
        return b


def minimum(a, b):
    if a < b:
        return a
    else:
        return b


def teadad_prime(avali, akhari):
    count = 0
    enteha = maximum(avali, akhari)
    ebteda = minimum(avali, akhari)
    for num in range(ebteda, enteha + 1):
        if prime(num):
            count += 1
    return count


count = teadad_prime(avali, akhari)

if avali <= akhari:
    print(f'main order - amount: {count}')
else:
    print(f'reverse order - amount: {count}')
