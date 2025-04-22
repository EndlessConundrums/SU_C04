#class Person:
    #def __init__(self,name,age):
        #self.name = name
        #self.age = age
    
    #def say_info(self):
        #print(self.name)
        #print(self.age)
    
    #def aging(self,years):
        #for i in range(years):
            #self.age += 1
            #print("Happy birthday! " + self.name + " is turning " + str(self.age) + " years old this year.")
class Dog:
    def __init__(self,name):
        self.name = str(name)
    
    def play(self):
        print(self.name + " has spent 2 hours playing!")

    def sleep(self):
        print(self.name + " has slept for 2 hours. They is incredibly cute.")
    
    def day_cycle(self):
        self.play()
        self.play()
        self.play()
        self.sleep()
        self.play()
        self.play()
        self.sleep()

class Puppy(Dog):
    def day_cycle(self):
        self.play()
        self.sleep()
        self.play()
        self.sleep()
        self.play()
        self.sleep()
        self.sleep()

silly = Puppy("Sam")
serious = Dog("Rex")