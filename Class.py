class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def say_info(self):
        print(self.name)
        print(self.age)
    
    def aging(self,years):
        for i in range(years):
            self.age += 1
            print("Happy birthday! " + self.name + " is turning " + str(self.age) + " years old this year.")