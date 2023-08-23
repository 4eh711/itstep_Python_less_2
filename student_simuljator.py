import random

class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive =True
        self.truble = True
        self.money = 50

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -=3

    def to_sleep(self):
        print("Time To Slip")
        self.gladness +=3

    def to_chill(self):
        print("Rest time")
        self.progress -=0.1
        self.gladness +=5
        self.money -=5

    def to_work(self):
        print("Work time")
        self.progress +=0.2
        self.money +=10


    def is_alive(self):
        if self.progress < -0.5:
            print("Cast Out...")
            self.alive = False
        elif self.gladness <=0:
            print("Depressin...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.progress <-0.1:
            print("Go to study man!!!")
            self.alive = False
        elif self.money <= 10:
            print("GO to Work Man!!!")
            self.alive = False

    #def if_truble(self):
       # if self.progress <-0.1:
        #    print("Go to study man!!!")

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day" +str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,4)
        if live_cube == 1:
            self.to_study()
        elif live_cube ==2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube ==4:
            self.to_work()
        self.end_of_day()
        self.is_alive()

nick = Student(name = "Nick")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)


