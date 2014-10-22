from weapon import Weapon


class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.equipped_weapon = None

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

        if self.health + healing_points < self._MAX_HEALTH:
            self.health += healing_points
        else:
            self.health = self._MAX_HEALTH

        return True

    def has_weapon(self):
        return self.equipped_weapon is not None

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon

    def attack(self):
        if self.equipped_weapon is None:
            return 0
        return self.equipped_weapon.damage
