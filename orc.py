from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = self._normalize_berserk_factor(berserk_factor)

    def _normalize_berserk_factor(self, berserk_factor):
        if berserk_factor >= 1 and berserk_factor <= 2:
            return berserk_factor
        elif berserk_factor < 1:
            return 1
        elif berserk_factor > 2:
            return 2

    def attack(self):
        return self.berserk_factor * Entity.attack(self)
