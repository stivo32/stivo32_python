__author__ = 'k_eryomenko'
#creating an exception

try:
    x =5/0
except ZeroDivisionError as e:
    print(e)

#raise an exception
def getInput():
    userInput = input("Please, enter something: ")
    if len(userInput) ==0:
        raise IOError("There is no input")


getInput()


