import random

class Hamster():
    def __init__(self, hunger, thirst, love):
        self.hunger = hunger
        self.thirst = thirst
        self.love = love
        self.alive = True
        self.euthanize = False

    def feed(self):
        self.food = 100

    def water(self):
        self.water = 100

    def care(self):
        self.love = 100
        
    cuddle = care
    kiss = care

    def check(self):
        status = f"hunger: {self.hunger}%\nthirst: {self.thirst}%\nlove: {self.love}%"
        print(status)

    def kill(self):
        self.euthanize = True
      
    def update(self):
        hunger = self.hunger
        thirst = self.thirst
        love = self.love
        
        if not hunger or not thirst or not love:
            self.alive = False
                
            if thirst and love:
                print("Hamtaro died of hunger! You feel shame.")
                
            elif love and hunger:
                print("Hamtaro died of thirst! You feel shame.")
                
            elif hunger and thirst:
                print("Hamtaro died of emotional neglect! You feel shame.")

            elif hunger or thirst or love:
                print("Hamtaro died of multiple causes! You feel shame.")
                
        if self.euthanize == True:
            self.alive = False
            print("Hamtaro died from euthanasia. You feel shame.")


            

        
def rand():
    return random.randrange(1,100)
    
hamtaro = Hamster(rand(), rand(), rand())

print("this is hamtaro, please take care of him. You can type commands to interact with hamtaro. type '?' for a list of commands.")
while hamtaro.alive:

    
    command = input("What will you do?\n")

    if command == "feed":
        hamtaro.feed()
        print("You refill hamtaro's food, restoring his hunger.")
        
    elif command == "water":
        hamtaro.water()
        print("You refill hamtaro's water, restoring his thirst.")
        
    elif command == "cuddle":
        hamtaro.cuddle()
        print("You cuddle with hamtaro, restoring his love.")

    elif command == "kiss":
        hamtaro.kiss()
        print("You give hamtaro a kiss on the head, restoring his love.")

    elif command == "check":
        hamtaro.check()
        
    elif command == "kill":
        hamtaro.kill()

    elif command == "time":
        lower_limit = lambda val: int((abs(val)+val)/2)

        hamtaro.hunger = lower_limit(hamtaro.hunger - 10)
        hamtaro.thirst = lower_limit(hamtaro.thirst - 10)
        hamtaro.love = lower_limit(hamtaro.love - 10)
        
        
    elif command == "?":
        print("feed: raises hamtaro's hunger to 100%.\nwater: raises hamtaro's thirst to 100%.\ncuddle or kiss: raises hamtaro's love to 100%.\ncheck: displays hamtaro's vitals.\nkill: puts hamtaro out of his misery.")
     
    else:
        print("unknown command")

    hamtaro.update()
