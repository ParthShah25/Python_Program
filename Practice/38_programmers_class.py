class Programmer:
    company = "Microsoft"

    def __init__(self, name1, name2, name3, name4):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4

    def printing(self):
        print(f"The Name of Employee who works in {Programmer.company} is {name.name1}")
        print(f"The Name of Employee who works in {Programmer.company} is {name.name2}")
        print(f"The Name of Employee who works in {Programmer.company} is {name.name3}")
        print(f"The Name of Employee who works in {Programmer.company} is {name.name4}")

name = Programmer("Parth", "Harsh", "Devanshi", "Niharika")
name.printing()


