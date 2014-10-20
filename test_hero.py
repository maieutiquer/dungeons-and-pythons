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


if __name__ == '__main__':
    unittest.main()
