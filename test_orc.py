import unittest
from orc import Orc


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hell_orc = Orc("Hell", 100, 1.4)

    def test_attributes(self):
        self.assertEqual(1.4, self.hell_orc.berserk_factor)

    def test_berserk_over(self):
        self.assertRaises(ValueError, Orc, "My Orc", 100, 3)

    def test_berserk_under(self):
        self.assertRaises(ValueError, Orc, "My Orc", 100, 0.4)


if __name__ == '__main__':
    unittest.main()
