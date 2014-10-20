class Orc:

    def __init__(self, name, health, berserk_factor):
        self.name = name
        self.health = health
        self.berserk_factor = self.__set_berserk_factor(berserk_factor)
        self.__MAX_HEALTH = health

    def __set_berserk_factor(self, berserk_factor):
        if berserk_factor >= 1 and berserk_factor <= 2:
            return berserk_factor
        else:
            raise ValueError

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage_points):
        if self.health > damage_points:
            self.health -= damage_points
        else:
            self.health = 0

    def take_healing(self, healing_points):

        if not self.is_alive():
            return False

        if self.health + healing_points < self.__MAX_HEALTH:
            self.health += healing_points
        else:
            self.health = self.__MAX_HEALTH

        return True
