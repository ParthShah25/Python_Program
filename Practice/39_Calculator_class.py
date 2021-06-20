from math import *
class Calculator:

    def __init__(self, num):
        self.num = num

    def sq(self):
        print(f"The squre of the {self.num} is: {self.num ** 2}")

    def sqrtnum(self):
        print(f"The squre root of the {self.num} is: {sqrt(self.num)}")

    def cube(self):
        print(f"The cube of the {self.num} is: {self.num ** 3}")

number = Calculator(16)
number.sq()
number.sqrtnum()
number.cube()