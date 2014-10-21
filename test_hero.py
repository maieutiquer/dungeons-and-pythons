import unittest
from hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "Dragonslayer")

    def test_attributes(self):
        self.assertEqual("Dragonslayer", self.bron_hero.nickname)

    def test_known_as(self):
        self.assertEqual("Bron the Dragonslayer", self.bron_hero.known_as())


if __name__ == '__main__':
    unittest.main()
