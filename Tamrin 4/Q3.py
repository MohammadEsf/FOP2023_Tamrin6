invalidCommand = 'Invalid Command.'
errorHasOccurred = False


class Player:
    health = -1
    name = ''
    score = 0

    def __init__(self, health, name):
        self.health = health
        self.name = name


nameOfPlayers = input().split()

healthOfPlayers = []
try:
    a = list(map(int, input().split()))
    for health in a:
        healthOfPlayers.append(health)
except:
    errorHasOccurred = True

damageOfCards = dict()

try:
    damageOfA, damageOfB, damageOfC = map(int, input().split())
    damageOfCards['A'] = damageOfA
    damageOfCards['B'] = damageOfB
    damageOfCards['C'] = damageOfC
except:
    errorHasOccurred = True

player1 = Player(healthOfPlayers[0], nameOfPlayers[0])
player2 = Player(healthOfPlayers[1], nameOfPlayers[1])

for i in range(3):
    cards = input().split()
    if errorHasOccurred:
        continue


    player1.health = player1.health - damageOfCards[cards[1]]
    player2.health = player2.health - damageOfCards[cards[0]]

    if damageOfCards[cards[0]] > damageOfCards[cards[1]]:
        player1.score = player1.score + 1
    else:
        player2.score = player2.score + 1

if errorHasOccurred:
    print(invalidCommand)
else:
    print(f'{player1.name} -> Score: {player1.score}, Health: {player1.health}')
    print(f'{player2.name} -> Score: {player2.score}, Health: {player2.health}')
