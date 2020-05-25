

import random

def sim():
    sim = int(input("Enter number of simulations: "))
    return(sim)

def cost():
    cost = float(input("Enter cost per roll: "))
    return(cost)

def get_things():
    pass

class Game:
    def __init__(self, sim, cost):
        self.sim = sim
        self.cost = cost

    def price_Of_Game(self):
        return(self.sim * self.cost)

    def roll_Payout(self):
        roll = 0
        for i in range(self.sim):
            roll += random.randint(1,6)
        return(roll)

    def get_Difference(self,p,c):
        return(p-c)


test = Game(10000, 4)
print(test.price_Of_Game())
print(test.roll_Payout())
print(test.get_Difference(test.price_Of_Game(),test.roll_Payout()))
