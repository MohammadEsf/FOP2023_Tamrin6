class Bimar:
    id = -1
    name = ''
    familyName = ''
    age = -1
    height = -1
    weight = -1
    visitTime = -1

    def __init__(self,id , name , familyName , age , height , weight):
        self.id = id
        self.name = name
        self.familyName = familyName
        self.age = age
        self.height = height
        self.weight = weight

    def setVisitTIme(self , time):
        self.visitTime = time


def idAlreadyExist(listOfBimar , idToCheck):
    for i in range(len(listOfBimar)):
        bimar = listOfBimar[i]
        if bimar.id == idToCheck:
            return True

    return False

def visitTimeAlreadyExists(listOfBimar , timeToCheck):
    for i in range(len(listOfBimar)):
        bimar = listOfBimar[i]
        if bimar.visitTime == timeToCheck:
            return True
    return False

def displayInfoOfBimar(id):
    for i in range(len(listOfBimar)):
        bimar = listOfBimar[i]
        if id == bimar.id:
            name = bimar.name
            familyName = bimar.familyName
            age = bimar.age
            height = bimar.height
            weight = bimar.weight

            print(f'patient name: {name}\npatient family name: {familyName}\npatient age: {age}\npatient height: {height}\npatient weight: {weight}')
            return

    print('error: invalid ID')


def gharareMolaqat(orderOfMolaqat , listOfBimar , id , visitTime):
    if not idAlreadyExist(listOfBimar , id):
        print('error: invalid id')
        return

    if visitTime<9 or visitTime > 18:
        print('error: invalid time')
        return

    if visitTimeAlreadyExists(listOfBimar,visitTime):
        print('error: busy time')
        return


    for i in range(len(listOfBimar)):
        bimar = listOfBimar[i]
        if bimar.id == id:
            bimar.setVisitTIme(visitTime)
            orderOfMolaqat.append(bimar.id)
            break
    print('visit added successfully!')

def removeBimar(listOfBimar , id):
    for i in range(len(listOfBimar)):
        bimar = listOfBimar[i]
        if bimar.id == id:
            listOfBimar.pop(i)
            print('patient deleted successfully!')

def displayMolaqatByID(listOfBimar , idToDisplay):
    for i in range(len(listOfBimar)):
        bimar = listOfBimar[i]
        if idToDisplay == bimar.id:
            formattedVisitTime = str(bimar.visitTime).zfill(2) + ":00"
            print(f'{formattedVisitTime} {bimar.name} {bimar.familyName}')


def displayVisitTimes(orderOfMolaqat , listOfBimar):
    print('SCHEDULE:')
    for i in range(len(orderOfMolaqat)):
        molaqatId = orderOfMolaqat[i]
        displayMolaqatByID(listOfBimar , molaqatId)


listOfBimar =[]
orderOfMolaqat = []

while True:
    command = input()

    if command == 'exit':
        break

    command = command.split()

    if command[0] == 'add' and command[1] == 'patient':
        id = int(command[2])

        if idAlreadyExist(listOfBimar, id):
            print('error: this ID already exists')
            continue


        name = command[3]
        familyName = command[4]

        age = int(command[5])
        if age < 0:
            print('error: invalid age')
            continue


        height = int(command[6])
        if height < 0:
            print('error: invalid height')
            continue

        weight = int(command[7])
        if weight < 0:
            print('error: invalid weight')
            continue

        bimar = Bimar(id , name , familyName , age , height , weight)


        listOfBimar.append(bimar)
        print('patient added successfully')

    elif command[0] == 'display' and command[1] == 'patient':
        id = int(command[2])
        displayInfoOfBimar(id)

    elif command[0] == 'add' and command[1] == 'visit':
        id = int(command[2])
        visitTime = int(command[3])
        gharareMolaqat(orderOfMolaqat , listOfBimar,id , visitTime)

    elif command[0] == 'delete' and command[1] == 'patient':
        id = int(command[2])
        if not idAlreadyExist(listOfBimar,id):
            print('error: invalid id')
            continue
        removeBimar(listOfBimar , id)

    elif command[0] == 'display' and command[1] == 'visit' and command[2] == 'list':
        displayVisitTimes(orderOfMolaqat , listOfBimar)

    else:
        print('invalid command')




