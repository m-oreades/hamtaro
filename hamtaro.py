import json
import time

#hamster
class Hamster():
    # init
    def __init__(self,
                 hunger = 50,
                 thirst = 50,
                 love = 50,
                 birthday = int(time.time()/10),
                 last_checked = int(time.time()/10),
                 alive = True):
        
        self.hunger = hunger
        self.thirst = thirst
        self.love = love
        self.birthday = birthday
        self.last_checked = last_checked
        self.alive = True 

    # feed
    def feed(self):
        if self.hunger < 100:
            self.hunger = 100
            print("You refill hamtaro's food, restoring his hunger.")
        else:
            print("Hamtaro's food dish is already full!")
    
    # water
    def water(self):
        if self.thirst < 100:
            self.thirst = 100
            print("You refill hamtaro's water, restoring his thirst.")
        else:
            print("Hamtaro's water bottle is already full!")

    # care
    def care(self, affection_type):
        if self.love < 100:
            self.love = 100

            if affection_type == "cuddle":
                print("You cuddle with hamtaro, restoring his love.")

            elif affection_type == "kiss":
                print("You give Hamtaro a kiss on the head, restoring his love.")
        else:
            print("Hamtaro already feels completely loved!")  
    cuddle = care
    kiss = care

    # check
    def check(self):
        self.health_update()
        if self.hunger == 0 or self.thirst == 0 or self.love == 0:
            self.die()

        status = f"hunger: {self.hunger}%\nthirst: {self.thirst}%\nlove: {self.love}%"
        print(status)

    # kill
    def kill(self):
        print("Hamtaro died from euthanasia. You feel shame.")
        self.die()
    
    # die
    def die(self):
        self.alive = False
        with open('data.json', 'w') as f:
            json.dump({}, f)

    #zero_limit
    def zero_limit(self,attribute):
        if attribute < 0:
            attribute = 0
        return attribute

    # health update
    def health_update(self):
        current_time = int(time.time()/10)
        difference = current_time - self.last_checked
        self.last_checked = current_time

        self.hunger -= difference
        self.thirst -= difference
        self.love -= difference

        self.hunger = self.zero_limit(self.hunger)
        self.thirst = self.zero_limit(self.thirst)
        self.love = self.zero_limit(self.love)

    # check life
    def check_life(self):
        starve = False
        dehydrate = False
        neglect = False
        
        if self.hunger <= 0:
            starve = True 
            
        if self.thirst <= 0:
            dehydrate = True
   
        if self.love <= 0:
            neglect = True
         
        # if any of the 3 health attributes reach 0:
        if starve == True or dehydrate == True or neglect == True:

            self.die()
            
            # if hunger is the only attribute that reached 0:
            if dehydrate == False and neglect == False:
                print("Hamtaro died of hunger! You feel shame.")

            # if thirst is the only attribute that reached 0:
            elif starve == False and neglect == False:
                print("Hamtaro died of thirst! You feel shame.")
            
            # if love is the only attribute that reached 0:    
            elif starve == False and dehydrate == False:
                print("Hamtaro died of emotional neglect! You feel shame.")

            # more than one attribute reached 0:
            else:
                print("Hamtaro died of multiple causes! You feel shame.")

    # update
    def update(self):

        self.health_update()
        
        self.check_life()
        if self.alive == True:
            write(self)
       
#command_process
def command_process():
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
        
    elif command == "?":
        print("feed: raises hamtaro's hunger to 100%.\nwater: raises hamtaro's thirst to 100%.\ncuddle or kiss: raises hamtaro's love to 100%.\ncheck: displays hamtaro's vitals.\nkill: puts hamtaro out of his misery.\nquit: exits the game.")

    elif command == "quit":
        exit()
        
    else:
        print("unknown command")
    
#read
def read():
    with open('data.json') as f:      
        data = json.load(f)
        if data == {}:
            # default starting point
            return Hamster()
        else:
            return Hamster(**data)

#write
def write(obj):
    
    with open('data.json', 'w') as f:
        json.dump(vars(obj), f, indent=2)

if __name__ == '__main__':

    # use attributes from json to create hamster
    hamtaro = read()
    
    print("this is hamtaro, please take care of him. You can type commands to interact with hamtaro. type '?' for a list of commands.")
    while hamtaro.alive:
        command_process()
        hamtaro.update()
        
        


