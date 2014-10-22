import unittest
from weapon import Weapon


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.axe = Weapon("Axe", 10, 0.2)

    def test_attributes(self):
        self.assertEqual("Axe", self.axe.type)
        self.assertEqual(10, self.axe.damage)
        self.assertEqual(0.2, self.axe.critical_strike_percent)

    def test_critical_hit_never(self):
        self.axe.critical_strike_percent = 0
        damage_values = []

        for x in range(1, 10000):
            current_damage = self.axe.critical_hit()
            damage_values.append(current_damage)

        self.assertFalse(20 in damage_values)

    def test_critical_hit_always(self):
        self.axe.critical_strike_percent = 1
        damage_values = []

        for x in range(1, 10000):
            current_damage = self.axe.critical_hit()
            damage_values.append(current_damage)

        self.assertFalse(10 in damage_values)

    def test_critical_hit_sometimes(self):
        self.axe.critical_strike_percent = 1
        damage_values = []

        for x in range(1, 10000):
            current_damage = self.axe.critical_hit()
            damage_values.append(current_damage)

        self.assertFalse(10 in damage_values)


if __name__ == '__main__':
    unittest.main()
