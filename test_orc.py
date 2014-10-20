import unittest
from orc import Orc


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hell_orc = Orc("Hell", 100, 1.4)

    def test_attributes(self):
        self.assertEqual("Hell", self.hell_orc.name)
        self.assertEqual(100, self.hell_orc.health)
        self.assertEqual(1.4, self.hell_orc.berserk_factor)

    def test_berserk_over(self):
        self.assertRaises(ValueError, Orc, "My Orc", 100, 3)

    def test_get_health(self):
        self.hell_orc.health = 80
        self.assertEqual(80, self.hell_orc.get_health())

    def test_is_alive(self):
        self.hell_orc.health = 80
        self.assertTrue(self.hell_orc.is_alive())

    def test_is_dead(self):
        self.hell_orc.health = 0
        self.assertFalse(self.hell_orc.is_alive())

    def test_take_damage_survive(self):
        self.hell_orc.health = 100
        self.hell_orc.take_damage(30)
        self.assertEqual(70, self.hell_orc.get_health())
        self.assertTrue(self.hell_orc.is_alive())

    def test_take_damage_die(self):
        self.hell_orc.health = 100
        self.hell_orc.take_damage(110)
        self.assertEqual(0, self.hell_orc.get_health())
        self.assertFalse(self.hell_orc.is_alive())

    def test_take_damage_die_exact(self):
        self.hell_orc.health = 50
        self.hell_orc.take_damage(50)
        self.assertEqual(0, self.hell_orc.get_health())
        self.assertFalse(self.hell_orc.is_alive())

    def test_take_healing_regular(self):
        self.hell_orc.health = 40
        self.hell_orc.take_healing(20)
        self.assertEqual(60, self.hell_orc.get_health())
        self.assertTrue(self.hell_orc.is_alive())

    def test_take_healing_overheal(self):
        self.hell_orc.health = 90
        self.assertTrue(self.hell_orc.take_healing(20))
        self.assertEqual(100, self.hell_orc.get_health())
        self.assertTrue(self.hell_orc.is_alive())

    def test_take_healing_overheal_exact(self):
        self.hell_orc.health = 90
        self.assertTrue(self.hell_orc.take_healing(10))
        self.assertEqual(100, self.hell_orc.get_health())
        self.assertTrue(self.hell_orc.is_alive())

    def test_take_healing_dead(self):
        self.hell_orc.health = 0
        self.assertFalse(self.hell_orc.take_healing(20))
        self.assertEqual(0, self.hell_orc.get_health())
        self.assertFalse(self.hell_orc.is_alive())



if __name__ == '__main__':
    unittest.main()
