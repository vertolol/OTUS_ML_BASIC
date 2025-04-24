import unittest

from homework_06.exceptions import CargoOverload
from homework_06.plane import Plane


class TestPlane(unittest.TestCase):
    def setUp(self):
        self.plane = Plane(weight=1000, fuel=50, fuel_consumption=10, max_cargo=100)

    def test_load_cargo_with_enough_space(self):
        self.plane.load_cargo(50)
        self.assertEqual(self.plane.cargo, 50)

    def test_load_cargo_with_not_enough_space(self):
        with self.assertRaises(CargoOverload):
            self.plane.load_cargo(150)

    def test_remove_all_cargo(self):
        self.plane.load_cargo(50)
        old_cargo = self.plane.remove_all_cargo()
        self.assertEqual(old_cargo, 50)
        self.assertEqual(self.plane.cargo, 0)

    def test_remove_all_cargo_with_no_cargo(self):
        old_cargo = self.plane.remove_all_cargo()
        self.assertEqual(old_cargo, 0)
        self.assertEqual(self.plane.cargo, 0)


if __name__ == '__main__':
    unittest.main()
