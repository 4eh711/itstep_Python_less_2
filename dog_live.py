import random

class Dog:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.hungry = 0
        self.alive =True
        self.truble = True


    def to_eat(self):
        print("Time to eat")
        self.hungry += 0.12
        self.gladness +=3

    def to_sleep(self):
        print("Time To Sleep")
        self.gladness +=5

    def to_play(self):
        print("Playing time")
        self.hungry -=0.05
        self.gladness +=5


    def is_alive(self):
        if self.hungry < -0.5:
            print("I'm dying...")
            self.alive = False
        elif self.gladness <=0:
            print("Depressin...")
            self.alive = False
        elif self.hungry > 5:
            print("I want to sleep...")
            self.alive = False


    #def if_truble(self):
       # if self.progress <-0.1:
        #    print("Go to study man!!!")

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Hungry = {round(self.hungry,2)}")

    def live(self, day):
        day = "Day" +str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube ==2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_play()
        self.end_of_day()
        self.is_alive()

reks = Dog(name = "Reks")

for day in range(365):
    if reks.alive == False:
        break
    reks.live(day)