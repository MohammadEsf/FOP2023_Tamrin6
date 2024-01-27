import re

invalidCommandMessage = 'invalid command'
currentMenu = 'l'  # l -> login menu    s -> student menu    p -> professor menu
especialCharacters = ["*", ".", "!", "@", "$", "%", "^", "&", "(", ")"]
allUsers = []
allCourses = []
loggedInUser = None

#############################  REGEXES   ##########################

exitRegex = r'edu exit edu'
showCurrentMenuRegex = r'edu current menu edu'
signUpRegex = r'edu sign up -(.+) -i (.+) -n (.+) -p (.+) edu'
loginRegex = r'edu log in -i (.+) -p (.+) edu'
showCourseListRegex = r'edu show course list edu'
logoutRegex = r'edu log out edu'
addCourseRegex = r'edu add course -c (.+) -i (.+) -n (.+) edu'
getCourseRegex = r'edu get course -i (.+) edu'


######################################################################
####################   CLASSES      ##############################

class User:


    def __init__(self, id, name, password, type):
        self.id = id
        self.name = name
        self.password = password
        self.type = type
        self.coursesTaken_IDs = []


class Course:
    def __init__(self, capacity, name, courseId, numberOfStudents):
        self.capacity = capacity
        self.name = name
        self.courseId = courseId
        self.numberOfStudents = numberOfStudents


######################################################################
######################################################################

def printCurrentMenu():
    if currentMenu == 'l':
        print('log in/sign up menu')
    elif currentMenu == 's':
        print('student menu')
    else:
        print('professor menu')


######################################################################
##################  SIGN UP METHODS   ################################
def passwordContainsSpecialChars(password):
    for c in especialCharacters:
        if c in password:
            return True
    return False


def userIdIsDuplicated(idToCheck):
    for user in allUsers:
        if user.id == idToCheck:
            return True
    return False


def signUpAction(signUpType, signUpId, signUpName, signUpPassword):
    if signUpType != 'S' and signUpType != 'P':
        print('invalid type')
    elif not signUpId.isnumeric():
        print('invalid id')
    elif ' ' in signUpName:
        print('invalid name')
    elif len(signUpPassword) < 4 or ' ' in signUpPassword or not passwordContainsSpecialChars(signUpPassword):
        print('invalid password')
    elif userIdIsDuplicated(signUpId):
        print('id already exists')
    else:
        newUser = User(signUpId, signUpName, signUpPassword, signUpType)
        allUsers.append(newUser)
        print('signed up successfully!')


#######################################################################
#######################################################################


######################################################################
##################  LOGIN METHODS   ################################

def userIdExists(idToCheck):
    for user in allUsers:
        if user.id == idToCheck:
            return True
    return False


def loginAction(id, password):
    global currentMenu, loggedInUser

    if not userIdExists(id):
        print('incorrect id')
        return

    userToLogin = None
    for user in allUsers:
        if user.id == id:
            userToLogin = user
            break

    if userToLogin.password != password:
        print('incorrect password')
    else:
        loggedInUser = userToLogin
        print('logged in successfully!')
        if userToLogin.type == 'S':
            print('entered student menu')
            currentMenu = 's'
        else:
            print('entered professor menu')
            currentMenu = 'p'


######################################################################
######################  SHOW COURSES LIST  #################################

def showCoursesList():
    print('course list:')
    for course in allCourses:
        print(f'{course.courseId} {course.name} {course.numberOfStudents}/{course.capacity}')


######################################################################
###################### LOG OUT  #################################

def logoutAction():
    global currentMenu
    print('logged out successfully!\nentered log in/sign up menu')
    currentMenu = 'l'

###################################################################
###################  ADD COURSE  #################################

def courseIdIsDuplicated(idToCheck):
    for course in allCourses:
        if course.courseId == idToCheck:
            return True
    return False


def addCourseAction(courseName, courseId, capacity):
    if ' ' in courseName:
        print('invalid course name')
    elif not courseId.isnumeric():
        print('invalid course id')
    elif not capacity.isnumeric():
        print('invalid course capacity')
    elif courseIdIsDuplicated(courseId):
        print('course id already exists')
    else:
        newCourse = Course(int(capacity), courseName, courseId, 0)
        allCourses.append(newCourse)
        print('course added successfully!')


###################################################################
######################  GET COURSE   ##############################


def courseIdExists(idToCheck):
    for course in allCourses:
        if course.courseId == idToCheck:
            return True
    return False


def returnCourseById(id):
    for course in allCourses:
        if course.courseId == id:
            return course


def getCourseAction(courseId):
    global loggedInUser

    if not courseIdExists(courseId):
        print('incorrect course id')
        return
    if courseId in loggedInUser.coursesTaken_IDs:
        print('you already have this course')
        return
    courseToTake = returnCourseById(courseId)
    if courseToTake.numberOfStudents >= courseToTake.capacity:
        print('course is full')
    else:
        loggedInUser.coursesTaken_IDs.append(courseId)
        courseToTake.numberOfStudents += 1
        print('course added successfully!')



###################################################################
###################################################################

def runSystem():
    while True:
        command = input().strip()

        if re.search(exitRegex, command):
            return
        elif re.search(showCurrentMenuRegex, command):
            printCurrentMenu()
        elif re.findall(signUpRegex, command) and currentMenu == 'l':
            signUpType, signUpId, signUpName, signUpPassword = re.findall(signUpRegex, command)[0]
            signUpAction(signUpType, signUpId, signUpName, signUpPassword)
        elif re.findall(loginRegex, command) and currentMenu == 'l':
            id, password = re.findall(loginRegex, command)[0]
            loginAction(id, password)
        elif re.search(showCourseListRegex, command) and currentMenu != 'l':
            showCoursesList()
        elif re.search(logoutRegex, command) and currentMenu != 'l':
            logoutAction()
        elif re.findall(addCourseRegex, command) and currentMenu == 'p':
            courseName, courseId, capacity = re.findall(addCourseRegex, command)[0]
            addCourseAction(courseName, courseId, capacity)
        elif re.findall(getCourseRegex, command) and currentMenu == 's':
            courseId = re.findall(getCourseRegex, command)[0]
            getCourseAction(courseId)
        else:
            print(invalidCommandMessage)


###################################################################
###################################################################

runSystem()
