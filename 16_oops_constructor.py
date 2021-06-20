class Employee:

    def __init__(self, name, salary, job_role):
        self.name = name
        self.salary = salary
        self.job_role = job_role

a = Employee("Parth", "100k", "Python Developer")

# a.name = "Parth"
# a.salary = "100k"
# a.job_role = "Python Developer"

print(a.name)
print(a.salary)
print(a.job_role)