n = int(input())
def print_pascal(n):
    for line in range(1, n + 1):
        c = 1
        for i in range(1, line + 1):
            print(c, end=" ")
            c = c * (line - i) // i
        print()
print_pascal(n)