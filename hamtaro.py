import random

class Hamster():
    def __init__(self, hunger, thirst, love):
        self.hunger = hunger
        self.thirst = thirst
        self.love = love
        self.alive = True
        
        self.euthanize = False  
        self.starve = False
        self.dehydrate = False
        self.neglect = False


    def feed(self):
        if self.hunger < 100:
            self.hunger = 100
            print("You refill hamtaro's food, restoring his hunger.")
        else:
            print("Hamtaro is already full!")

    def water(self):
        if self.thirst < 100:
            self.thirst = 100
            print("You refill hamtaro's water, restoring his thirst.")
        else:
            print("Hamtaro is fully hydrated!")

    def care(self, affection):
        if self.love < 100:
            self.love = 100
            if affection == "cuddle":
                print("You cuddle with hamtaro, restoring his love.")
            elif affection == "kiss":
                print("You give Hamtaro a kiss on the head, restoring his love.")
        else:
            print("Hamtaro is already completely loved!")
        
    cuddle = care
    kiss = care

    def check(self):
        status = f"hunger: {self.hunger}%\nthirst: {self.thirst}%\nlove: {self.love}%"
        print(status)

    def kill(self):
        self.euthanize = True

    def check_life(self):
        if self.hunger <= 0:
            self.starve = True 
            
        if self.thirst <= 0:
            self.dehydrate = True
   
        if self.love <= 0:
            self.neglect = True
         
        if self.starve == True or self.dehydrate == True or self.neglect == True:
            
            self.alive = False
            
            if self.dehydrate == False and self.neglect == False:
                print("Hamtaro died of hunger! You feel shame.")
                
            elif self.starve == False and self.neglect == False:
                print("Hamtaro died of thirst! You feel shame.")
                
            elif self.starve == False and self.dehydrate == False:
                print("Hamtaro died of emotional neglect! You feel shame.")

            else:
                print("Hamtaro died of multiple causes! You feel shame.")
                
        if self.euthanize == True:
            self.alive = False
            print("Hamtaro died from euthanasia. You feel shame.")

            
    def update(self):
        self.check_life()
       
def rand():
    return random.randrange(1,100)
    
hamtaro = Hamster(rand(), rand(), rand())

if __name__ == '__main__':
    
    print("this is hamtaro, please take care of him. You can type commands to interact with hamtaro. type '?' for a list of commands.")
    while hamtaro.alive:

        
        command = input("What will you do?\n")

        if command == "feed":
            hamtaro.feed()         
            
        elif command == "water":
            hamtaro.water()           
            
        elif command == "cuddle" or command == "kiss":
            hamtaro.care(command)

        elif command == "check":
            hamtaro.check()
            
        elif command == "kill":
            hamtaro.kill()
            
## sleighted for removal
        elif command == "time":
            hamtaro.hunger -= 10
            hamtaro.thirst -= 10
            hamtaro.love -= 10
##
            
        elif command == "?":
            print("feed: raises hamtaro's hunger to 100%.\nwater: raises hamtaro's thirst to 100%.\ncuddle or kiss: raises hamtaro's love to 100%.\ncheck: displays hamtaro's vitals.\nkill: puts hamtaro out of his misery.\ntime: passes time and reduces all attributes by 10.\nquit: exits the game.")

        elif command == "quit":
            exit()
            
        else:
            print("unknown command")


        hamtaro.update()

