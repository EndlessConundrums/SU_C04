from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def print_all_info(self):
        self.get_area()
        self.get_perimeter()
        print("The shape's perimeter is " + str(self.get_perimeter()) + ", and the area is " + str(self.get_area()))

class Triangle(Shape):
    def __init__(self, width):
        self.width = width

    def get_area(self):
        self.area = (self.width ** 2) // 2
        return self.area

    def get_perimeter(self):
        self.perimeter = self.width * 3
        return self.perimeter

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def get_perimeter(self):
        self.perimeter = (self.width * 2) + (self.length * 2)
        return self.perimeter

    def get_area(self):
        self.area = self.width * self.height
        return self.area

class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.length = width