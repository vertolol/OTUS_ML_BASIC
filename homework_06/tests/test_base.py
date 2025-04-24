import unittest
from homework_06.base import Vehicle
from homework_06.exceptions import LowFuelError, NotEnoughFuel


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(weight=1000, fuel=50, fuel_consumption=10)

    def test_start_with_fuel(self):
        self.vehicle.start()
        self.assertTrue(self.vehicle.started)

    def test_start_without_fuel(self):
        self.vehicle.fuel = 0
        with self.assertRaises(LowFuelError):
            self.vehicle.start()

    def test_move_with_enough_fuel(self):
        self.vehicle.move(2)
        self.assertEqual(self.vehicle.fuel, 30)

    def test_move_without_enough_fuel(self):
        with self.assertRaises(NotEnoughFuel):
            self.vehicle.move(10)

    def test_move_with_zero_distance(self):
        self.vehicle.move(0)
        self.assertEqual(self.vehicle.fuel, 50)

if __name__ == '__main__':
    unittest.main()
