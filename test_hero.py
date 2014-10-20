import unittest
from hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "Dragonslayer")

    def test_attributes(self):
        self.assertEqual("Bron", self.bron_hero.name)
        self.assertEqual(100, self.bron_hero.health)
        self.assertEqual("Dragonslayer", self.bron_hero.nickname)

    def test_known_as(self):
        self.assertEqual("Bron the Dragonslayer", self.bron_hero.known_as())

    def test_get_health(self):
        self.bron_hero.health = 80
        self.assertEqual(80, self.bron_hero.get_health())

    def test_is_alive(self):
        self.bron_hero.health = 80
        self.assertTrue(self.bron_hero.is_alive())

    def test_is_dead(self):
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.is_alive())

    def test_take_damage_survive(self):
        self.bron_hero.health = 100
        self.bron_hero.take_damage(30)
        self.assertEqual(70, self.bron_hero.get_health())
        self.assertTrue(self.bron_hero.is_alive())

    def test_take_damage_die(self):
        self.bron_hero.health = 100
        self.bron_hero.take_damage(110)
        self.assertEqual(0, self.bron_hero.get_health())
        self.assertFalse(self.bron_hero.is_alive())

    def test_take_healing_regular(self):
        self.bron_hero.health = 40
        self.bron_hero.take_healing(20)
        self.assertEqual(60, self.bron_hero.get_health())
        self.assertTrue(self.bron_hero.is_alive())

    def test_take_healing_overheal(self):
        self.bron_hero.health = 90
        self.assertTrue(self.bron_hero.take_healing(20))
        self.assertEqual(100, self.bron_hero.get_health())
        self.assertTrue(self.bron_hero.is_alive())

    def test_take_healing_dead(self):
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.take_healing(20))
        self.assertEqual(0, self.bron_hero.get_health())
        self.assertFalse(self.bron_hero.is_alive())


if __name__ == '__main__':
    unittest.main()
