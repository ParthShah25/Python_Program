#single inheritance

# class Player:

#     def name(self,name):
#         self.name = name
#         print(f"The name of player is {self.name}")

# class Score(Player):

#     def runs(self,run):
#         self.run = run
#         print(f"{self.name} scored {self.run}")

# r = Score()
# r.name("Parth")
# r.runs(150)

#multiple inheritance

# class Player:

#     def name(self,name):
#         self.name = name
#         print(f"The name of player is {self.name}")

# class Score():

#     def runs(self,run):
#         self.run = run
#         print(f"{self.name} scored {self.run}")

# class Total(Player, Score):

#     def totalRun(self, tot):
#         self.tot = tot
#         print(f"{self.name} scored in an inning is {self.run} and his total runs are {self.tot} ")

# t = Total()
# t.name("Parth")
# t.runs(150)
# t.totalRun(5246)

#multilevel inheritance

class Player:
    country = "India"
    type = "Bowler"

    def __init__(self, name, run, tot):
        self.name = name
        self.run = run
        self.tot = tot

    def nam(self):
        print(f"The name of player is {self.name}")

class Score(Player):
    type = "Batsman"

    def runs(self):
        print(f"{self.name} scored {self.run} in an inning ")

class Total(Score):
    country = "South Africa"

    def totalRun(self):
        print(f"{self.name} scored in an inning is {self.run} and his total runs are {self.tot} ")

p = Player("Parth", 150, 5690)
print(p.country)
print(p.type)
p.nam()

s = Score("Parth", 150, 5690)
print(s.country)
print(s.type)
s.runs()

t = Total("Parth", 150, 5690)
print(t.country)
print(t.type)
t.totalRun()

# 10.55.30





