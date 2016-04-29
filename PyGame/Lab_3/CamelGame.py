import random
class CamelGame():
    def __init__(self):
        self.mileTraveled = 0
        self.thirst = 0
        self.camelTiredness = 0
        self.nativeTraveled = -20
        self.drinks = 3
        self.action=''

    def mainLoop(self):
        done = False
        startOfGameMessage = 'Welcome to Camel!\n'
        startOfGameMessage+='You have stolen a camel to make your way across the great Mobi desert.\n'
        startOfGameMessage+='The natives want their camel back and are chasing you down! Survive your\n'
        startOfGameMessage+='desert trek and out run the natives.\n'

        print(startOfGameMessage)

        choosingOfAction = 'A. Drink from your canteen.\n'
        choosingOfAction += 'B. Ahead moderate speed.\n'
        choosingOfAction += 'C. Ahead full speed.\n'
        choosingOfAction += 'D. Stop for the night.\n'
        choosingOfAction += 'E. Status check.\n'
        choosingOfAction += 'Q. Quit.\n'


        while not done:
            print(self.checkStatus())
            self.action = input(choosingOfAction)
            self.action = self.action.lower()
            if self.action == 'a':
                self.drink()
            elif self.action == 'b':
                self.moveModSpeed()
            elif self.action == 'c':
                self.moveFullSpeed()
            elif self.action == 'd':
                self.stopForRest()
            elif self.action == 'e':
                self.checkStatus()
            elif self.action == 'q':
                print('Game Over')
                done = True
            else:
                print('Wrong choise, choose one of the actions')

            if (not done and self.thirst > 6):
                print("You died of thirst. Game Over")
                done=True
                continue
            elif (not done and self.thirst > 4):
                print("You are thirsty")

            if (not done and self.camelTiredness > 8):
                print("Your camel is dead. Game Over")
                done=True
                continue
            elif (not done and self.camelTiredness > 5):
                print("Your camel if getting tired")

            if not done and (self.mileTraveled-self.nativeTraveled < 1):
                print("The Natives have cought you. Game Over")
                done = True
                continue
            elif not done and (self.mileTraveled-self.nativeTraveled < 15):
                print("The Natives are getting close")

            if not done and self.mileTraveled > 199:
                print("You've escaped from the desert. Congratulations!")
                done = True

    def checkStatus(self):
        status = 'Miles traveled: '+str(self.mileTraveled)+'\n'
        status += 'Drinks in canteen: '+str(self.drinks)+'\n'
        status += 'The natives are ' +(str(self.mileTraveled-self.nativeTraveled))+ ' miles behind you.''\n'
        return status

    def moveFullSpeed(self):
        self.mileTraveled+=random.randint(10,21)
        self.thirst+=1
        self.camelTiredness+=random.randint(1,4)
        self.moveNative()
        self.findOasis()

    def moveModSpeed(self):
        self.mileTraveled+=random.randint(5,13)
        self.thirst+=1
        self.camelTiredness+=1
        self.moveNative()
        self.findOasis()

    def stopForRest(self):
        self.camelTiredness = 0
        self.moveNative()
    
    def drink(self):
        if self.drinks>0:
            self.drinks -=1
            self.thirst = 0
            self.moveNative()
        else:
            print("Your cantoon is empty")

    def moveNative(self):
        self.nativeTraveled += random.randint(7,15)

    def findOasis(self):
        if random.randint(1,10) == 1:
            print("You found an Oasis!!")
            self.drinks = 3
            self.thirst = 0
            self.camelTiredness = 0

if __name__ == '__main__':
    game = CamelGame()
    game.mainLoop()