import re

n = int(input())
whoseTurnIsIt = 1
#########################################
############  REGEXES  #################

newSoldierRegex = r'new (.+) (.+) (.+) (.+)'
moveRegex = r'move (.+) (.+)'
attackRegex = r'attack (.+) (.+)'
infoRegex = r'info (.+)'


##########################################
############  CLASSES ##################

class Soldier:
    def __init__(self, id, health, x, y):
        self.id = id
        self.health = health
        self.x = int(x)
        self.y = int(y)


class Archer(Soldier):
    pass

class Melee(Soldier):
    pass

##########################################
##########################################
player1Troops = []
player2Troops = []


###########################################
############## CREATE NEW TROOP  ######################

def idIsDuplicated(idToCheck):
    listToCheck = None
    if whoseTurnIsIt == 1:
        listToCheck = player1Troops
    else:
        listToCheck = player2Troops

    for troop in listToCheck:
        if troop.id == idToCheck:
            return True
    return False


def createNewTroop(soldierType, soldierId, x, y):

    if idIsDuplicated(soldierId):
        print('duplicate tag')
        return
    newSoldier = None
    if soldierType == 'archer':
        newSoldier = Archer(soldierId, 100, x, y)
    else:
        newSoldier = Melee(soldierId, 100, x, y)

    listToAdd = None
    if whoseTurnIsIt == 1:
        listToAdd = player1Troops
    else:
        listToAdd = player2Troops
    listToAdd.append(newSoldier)
    nextTurn()


###########################################
############  MOVE TROOP   ####################

def moveTroop(soldierId, direction):
    listToMove = None
    if whoseTurnIsIt == 1:
        listToMove = player1Troops
    else:
        listToMove = player2Troops

    soldierToMove = None
    for soldier in listToMove:
        if soldier.id == soldierId:
            soldierToMove = soldier
            break

    if direction == 'up':
        if soldierToMove.y == 0:
            print('out of bounds')
        else:
            soldierToMove.y -= 1
            nextTurn()
    elif direction == 'down':
        if soldierToMove.y == n - 1:  # TODO: MAYBE n
            print('out of bounds')
        else:
            soldierToMove.y += 1
            nextTurn()
    elif direction == 'left':
        if soldierToMove.x == 0:
            print('out of bounds')
        else:
            soldierToMove.x -= 1
            nextTurn()
    elif direction == 'right':
        if soldierToMove.x == n - 1:
            print('out of bounds')
        else:
            soldierToMove.x += 1
            nextTurn()


###########################################
#############  ATTACK  ##################

def manhatanDistance(soldier1, soldier2):
    return abs(soldier1.x - soldier2.x) + abs(soldier1.y - soldier2.y)


def attack(attackerId, targetId):
    global player1Troops , player2Troops
    listToAttack, listToBeAttacked = None, None
    if whoseTurnIsIt == 1:
        listToAttack = player1Troops
        listToBeAttacked = player2Troops
    else:
        listToAttack = player2Troops
        listToBeAttacked = player1Troops

    troopToAttack, troopToBeAttacked = None, None
    for troop in listToAttack:
        if troop.id == attackerId:
            troopToAttack = troop
            break
    for troop in listToBeAttacked:
        if troop.id == targetId:
            troopToBeAttacked = troop
            break

    distance = manhatanDistance(troopToAttack, troopToBeAttacked)
    if isinstance(troopToAttack, Archer):
        if distance > 2:
            print('the target is too far')
            return
        else:
            troopToBeAttacked.health -= 10
            if troopToBeAttacked.health <= 0:
                print('target eliminated')

                newList = []
                for troop in listToBeAttacked:
                    if troop.id != troopToBeAttacked.id:
                        newList.append(troop)

                if whoseTurnIsIt == 1:
                    player2Troops = newList
                else:
                    player1Troops = newList
    else:
        if distance > 1:
            print('the target is too far')
            return
        else:
            troopToBeAttacked.health -= 20
            if troopToBeAttacked.health <= 0:
                print('target eliminated')
                listToBeAttacked.remove(troopToBeAttacked)

    nextTurn()


###########################################
###########################################


def nextTurn():
    global whoseTurnIsIt
    if whoseTurnIsIt == 1:
        whoseTurnIsIt = 2
    else:
        whoseTurnIsIt = 1


###########################################
###########################################

def soldierExists(listToShow, id):
    for soldier in listToShow:
        if soldier.id == id:
            return True
    return False


def showInfo(soldierId):
    listToShow = None
    if whoseTurnIsIt == 1:
        listToShow = player1Troops
    else:
        listToShow = player2Troops

    if not soldierExists(listToShow, soldierId):
        print('soldier does not exist')
        return

    soldierToShow = None
    for soldier in listToShow:
        if soldier.id == soldierId:
            soldierToShow = soldier
            break

    print(f'health: {soldierToShow.health}')
    print(f'location: {soldierToShow.x} {soldierToShow.y}')

    nextTurn()


##########################################
##########################################

def sumOfHealths(listOfTroops):
    result = 0
    for troop in listOfTroops:
        result += troop.health
    return result


#########################################
#########################################


def play():
    while True:
        command = input()

        if command == 'end':
            return
        elif re.findall(newSoldierRegex, command):
            soldierType, soldierId, x, y = re.findall(newSoldierRegex, command)[0]
            createNewTroop(soldierType, soldierId, x, y)
        elif re.findall(moveRegex, command):
            soldierId, direction = re.findall(moveRegex, command)[0]
            moveTroop(soldierId, direction)
        elif re.findall(attackRegex, command):
            attackerId, targetId = re.findall(attackRegex, command)[0]
            attack(attackerId, targetId)
        elif re.findall(infoRegex, command):
            soldierId = re.findall(infoRegex, command)[0]
            showInfo(soldierId)
        elif command == 'who is in the lead?':
            player1score = sumOfHealths(player1Troops)
            player2score = sumOfHealths(player2Troops)

            if player1score == player2score:
                print('draw')
            elif player1score > player2score:
                print('player  1')
            else:
                print('player  2')


##########################################
##########################################
play()
