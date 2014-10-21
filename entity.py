class Entity:

    def __init__(self, name, health):

        self.name = name
        self.health = health
        self.__MAX_HEALTH = health

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
