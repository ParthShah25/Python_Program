# class Number:
#     def sum(self, a, b):
#         self.a = a
#         self.b = b
#         return self.a + self.b

# num = Number()
# s = num.sum(10,23)
# print(s)

class Employee:
    company = "Google"
    Role = "Software Engineer"

Parth = Employee()
Shruti = Employee()
print(Parth.company)
print(Shruti.company)

# Instance attribute : first take the value from Instance variable and if there is not define any instance object then they take the value from the class object

Parth.Role = "Testing manager" #here we define the object for Parth then they take the value from the instance object and Shruti take the value from the class object.

print(Parth.Role)
print(Shruti.Role)

# How to change company name 

Employee.company = "TCS"
print(Parth.company)
print(Shruti.company)
