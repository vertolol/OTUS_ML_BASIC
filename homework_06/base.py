from abc import ABC

from homework_06.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
    weight (int): Вес транспортного средства.
    started (bool): Состояние запуска транспортного средства.
    fuel (int): Количество топлива в транспортном средстве.
    fuel_consumption (int): Расход топлива транспортного средства.

    Методы:
    start(): Запускает транспортное средство, если есть топливо.
    move(distance): Перемещает транспортное средство на указанное расстояние, если есть достаточно топлива.
    """

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        """
        Инициализирует объект Vehicle.

        Аргументы:
        weight (int): Вес транспортного средства.
        fuel (int): Количество топлива в транспортном средстве.
        fuel_consumption (int): Расход топлива транспортного средства.
        """
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """
        Запускает транспортное средство, если есть топливо.

        Если топлива нет, выкидывает исключение LowFuelError.
        """
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Low fuel error")

    def move(self, distance):
        """
        Перемещает транспортное средство на указанное расстояние, если есть достаточно топлива.

        Аргументы:
        distance (int): Расстояние, на которое нужно переместить транспортное средство.

        Если топлива недостаточно, выкидывает исключение NotEnoughFuel.
        """
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel("Not enough fuel")
