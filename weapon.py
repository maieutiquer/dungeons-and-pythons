import random


class Weapon:

    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        if self.critical_strike_percent > random.random():
            return 2 * self.damage
        else:
            return self.damage
