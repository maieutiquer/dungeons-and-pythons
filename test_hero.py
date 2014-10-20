import unittest
from hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.new_hero = Hero("Bron", 100, "Dragonslayer")

    def test_attr(self):
        self.assertEqual("Bron", self.new_hero.name)
        self.assertEqual(health, self.new_hero.name)


if __name__ == '__main__':
    unittest.main()
