from entity.py import Entity


class Hero(Entity):

    def __init__(self, name, health, nickname):

        self.nickname = nickname

    def known_as(self):

        return "{} the {}".format(self.name, self.nickname)

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
