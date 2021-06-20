class Train:

    def __init__(self, name, number, email, seats, home, dest):
        self.name = name
        self.number = number
        self.email = email
        self.seats = seats
        self.home = home
        self.dest = dest   

    def booking(self):
        print(f"the name of passanger is {self.name}")
        print(f"the number of passanger is {self.number}")
        print(f"the email of passanger is {self.email}")

    def getStatus(self):
        print(f"The available seats is {self.seats}")

    def fareInfo(self):
        print(f"Passenger is travel from {self.home} to {self.dest}")

ticket = Train("Parth", "996554872", "parth@gmail.com", 12, "Surendranagar", "Mumbai")
ticket.booking()
ticket.getStatus()
ticket.fareInfo()
    