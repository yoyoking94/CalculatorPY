""" Import """
import numpy


def initMultiTable():
    print('')
    print("-------------------------------------")
    print("  Welcome to the Amazing Calculator  ")
    print("-------------------------------------")
    print('')


def mainMultiTable():
    inputChoice = input(
        "Choose your operation (addition or + | substraction or - | multiplication or x | division or / | exit to quit the program): ")
    """ print(inputChoice) """
    if inputChoice == "addition" or inputChoice == "+":
        Addition()
    elif inputChoice == "substraction" or inputChoice == "-":
        Substraction()
    elif inputChoice == "multiplication" or inputChoice == "x":
        Multiplication()
    elif inputChoice == "division" or inputChoice == "/":
        Division()
    elif inputChoice == "exit":
        exit()
    else:
        print("Watch out the spelling")
        mainMultiTable()


""" Addition """
def Addition():
    resAdd = 0
    tabAdd = []
    nbrValue = int(input('Enter the how many number you want to add : '))

    for i in range(nbrValue):
        tabAdd.append(int(input("Enter value : ")))

    resAdd = sum(tabAdd)
    print(tabAdd)
    print("the result is : ", resAdd)

    """ Restart the program """
    mainMultiTable()



""" Substraction """
def Substraction():
    resSub = 0
    tabSub = []
    nbrValue = int(input('Enter the how many number you want to substract : '))

    for i in range(nbrValue):
        tabSub.append(int(input("Enter value : ")))

    resSub = tabSub[0] - sum(tabSub[1:])
    print(resSub)
    print("the result is : ", resSub)

    # - Restart the program -#
    mainMultiTable()



""" Multiplication """
def Multiplication():
    resMulti = 1
    tabMulti = []
    nbrValue = int(input('Enter the how many number you want to substract : '))

    for i in range(nbrValue):
        tabMulti.append(int(input("Enter value : ")))

    resMulti = numpy.prod(tabMulti)

    print(resMulti)
    print("the result is : ", resMulti)
    
    #- Restart the program -#
    mainMultiTable()



""" Division """
def Division():
    print("")
    print('Choose two number to divided ')
    print("")
    value1 = int(input("Enter the first value : "))
    value2 = int(input("Enter the second value : "))
    print(value1,'+',value2,'=', value1/value2)
    
    #- Restart the program -#
    mainMultiTable()


""" Run function """
def runProgram():
    initMultiTable()
    mainMultiTable()


""" Start the game """
runProgram()
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:yoyoking94/LeJustePrix.git
git push -u origin main