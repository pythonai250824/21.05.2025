import math
import random
from argparse import ArgumentError
from typing import override


# circle
# get the radius in the __init__
# member hidden radius --> getter/ setter (check if bigger equals 0)
# make function get_area = math.pi*r^2
# make function get_perimeter = 2*math.pi*r
# make __str__

class Circle:

    # appear 1 time only in the class
    __pie = 3.14  # class variable (static)
    shape = '2d'  # class variable (static)

    def __init__(self, radius: float):
        self.radius = radius
        # self.__pie = 3.14

    # not in object
    @classmethod
    def get_pie(cls):
        # return Circle.__pie  # option-1.ok
        return cls.__pie  # option-2.better

    # not in object
    @staticmethod
    def description():
        # Circle.__pie  # works -- bad practice
        return "this is class shape..."

    @staticmethod
    def create_random_circle():
        return Circle(random.randint(100))

    @property
    def pie(self):
        return Circle.__pie

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            raise ArgumentError("radius should be positive")

    # cannot do setter without getter

    @property
    def area(self):
        return Circle.__pie * self.radius ** 2

    def get_area(self):
        return Circle.__pie* self.radius ** 2

    @override
    def __str__(self):
        return f"Circle radius={self.radius:.2f} area={self.get_area()}"

print(Circle.shape)

c1 = Circle(5)
c2 = Circle(2.5)
c3 = Circle(3.7)
c4 = Circle(8.9)
print(c1.radius)  # 5
print(f"{'c1.get_area()=':15}", c1.get_area())
print(f"{'c1.area=':15}", c1.area)

print(c1.shape)  # bad practice, not recommended
print(Circle.shape)  # better

print('c1.pie', c1.pie)

# static class
# object-class
class Car:
    type = 'Toyota'
    color = 'blue'

print(Car.color)
c1 = Car()
Car.color = 'black'


