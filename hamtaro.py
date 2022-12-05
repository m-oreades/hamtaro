import random



    
class Hamster():
    def __init__(self, hunger, thirst, love):
        self.hunger = hunger
        self.thirst = thirst
        self.love = love
        self.alive = True
        self.euthanize = False

    def feed(self):
        self.hunger = 100

    def water(self):
        self.thirst = 100

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

            else:
                print("Hamtaro died of multiple causes! You feel shame.")
                
        if self.euthanize == True:
            self.alive = False
            print("Hamtaro died from euthanasia. You feel shame.")
            


            

        
def rand():
    return random.randrange(1,100)
    
hamtaro = Hamster(rand(), rand(), rand())

if __name__ == '__main__':
    
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
            
            clamp_zero = lambda val: int((abs(val)+val)/2)

            hamtaro.hunger = clamp_zero(hamtaro.hunger - 10)
            hamtaro.thirst = clamp_zero(hamtaro.thirst - 10)
            hamtaro.love = clamp_zero(hamtaro.love - 10)
                   
        elif command == "?":
            print("feed: raises hamtaro's hunger to 100%.\nwater: raises hamtaro's thirst to 100%.\ncuddle or kiss: raises hamtaro's love to 100%.\ncheck: displays hamtaro's vitals.\nkill: puts hamtaro out of his misery.\ntime: passes time and reduces all attributes by 10.\nquit: exits the game.")

        elif command == "quit":
            exit()
            
        else:
            print("unknown command")

        hamtaro.update()

