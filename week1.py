class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

        
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


my_pet = Pet("Stormy")

my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.get_status()

my_pet.train("catch a ball")
my_pet.train("roll over")
my_pet.show_tricks()






