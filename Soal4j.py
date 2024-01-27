columnsNumber = int(input())

hasVisited = [[False] * columnsNumber for _ in range(1000)]
hasVisited[0][0] = True

positionI, positionJ = 0, 0

tedadePayeen = 1


def MoveRight():
    global positionJ
    if positionJ == columnsNumber - 1:
        return
    positionJ += 1
    hasVisited[positionI][positionJ] = True


def MoveDown():
    global positionI
    positionI += 1
    hasVisited[positionI][positionJ] = True


def MoveLeft():
    global positionJ
    if positionJ == 0:
        return
    positionJ -= 1
    hasVisited[positionI][positionJ] = True


while True:
    command = input()
    if command == 'END':
        break

    if command == 'R':
        MoveRight()
        # print(f'{positionI} {positionJ}')
    elif command == 'L':
        MoveLeft()
        # print(f'{positionI} {positionJ}')
    elif command == 'B':
        MoveDown()
        # print(f'{positionI} {positionJ}')

        tedadePayeen += 1

for i in range(tedadePayeen):
    for j in range(columnsNumber):
        if hasVisited[i][j]:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()

if positionJ != columnsNumber - 1:
    print("There's no way out!")
