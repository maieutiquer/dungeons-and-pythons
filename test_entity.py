import unittest
from entity import Entity


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity = Entity("NewEntity", 100)

    def test_attributes(self):
        self.assertEqual("NewEntity", self.entity.name)
        self.assertEqual(100, self.entity.health)

    def test_get_health(self):
        self.entity.health = 80
        self.assertEqual(80, self.entity.get_health())

    def test_is_alive(self):
        self.entity.health = 80
        self.assertTrue(self.entity.is_alive())

    def test_is_dead(self):
        self.entity.health = 0
        self.assertFalse(self.entity.is_alive())

    def test_take_damage_survive(self):
        self.entity.health = 100
        self.entity.take_damage(30)
        self.assertEqual(70, self.entity.get_health())
        self.assertTrue(self.entity.is_alive())

    def test_take_damage_die(self):
        self.entity.health = 100
        self.entity.take_damage(110)
        self.assertEqual(0, self.entity.get_health())
        self.assertFalse(self.entity.is_alive())

    def test_take_damage_die_exact(self):
        self.entity.health = 50
        self.entity.take_damage(50)
        self.assertEqual(0, self.entity.get_health())
        self.assertFalse(self.entity.is_alive())

    def test_take_healing_regular(self):
        self.entity.health = 40
        self.entity.take_healing(20)
        self.assertEqual(60, self.entity.get_health())
        self.assertTrue(self.entity.is_alive())

    def test_take_healing_overheal(self):
        self.entity.health = 90
        self.assertTrue(self.entity.take_healing(20))
        self.assertEqual(100, self.entity.get_health())
        self.assertTrue(self.entity.is_alive())

    def test_take_healing_overheal_exact(self):
        self.entity.health = 90
        self.assertTrue(self.entity.take_healing(10))
        self.assertEqual(100, self.entity.get_health())
        self.assertTrue(self.entity.is_alive())

    def test_take_healing_dead(self):
        self.entity.health = 0
        self.assertFalse(self.entity.take_healing(20))
        self.assertEqual(0, self.entity.get_health())
        self.assertFalse(self.entity.is_alive())


if __name__ == '__main__':
    unittest.main()
