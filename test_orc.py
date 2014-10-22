import unittest
from orc import Orc
from weapon import Weapon


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hell_orc = Orc("Hell", 100, 1.4)
        self.axe = Weapon("Axe", 10, 0.2)

    def test_attributes(self):
        self.assertEqual(1.4, self.hell_orc.berserk_factor)

    def test_berserk_over(self):
        self.assertEqual(2, self.hell_orc._normalize_berserk_factor(3))

    def test_berserk_under(self):
        self.assertEqual(1, self.hell_orc._normalize_berserk_factor(0.5))

    def test_attack(self):
        self.hell_orc.equip_weapon(self.axe)
        self.assertEqual(1.4 * self.hell_orc.equipped_weapon.damage,
                         self.hell_orc.attack())


if __name__ == '__main__':
    unittest.main()
