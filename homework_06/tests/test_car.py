import unittest
from homework_06.car import Car
from homework_06.engine import Engine


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(weight=1000, fuel=50, fuel_consumption=10)

    def test_set_engine_with_engine(self):
        engine = Engine(volume=2.0, pistons=4)
        self.car.set_engine(engine)
        self.assertEqual(self.car.engine, engine)

    def test_set_engine_without_engine(self):
        with self.assertRaises(ValueError):
            self.car.set_engine(None)

    def test_set_engine_with_non_engine(self):
        with self.assertRaises(ValueError):
            self.car.set_engine("Not an engine")


if __name__ == '__main__':
    unittest.main()
