from homework_06.base import Vehicle
from homework_06.exceptions import CargoOverload


class Plane(Vehicle):
    """
    Класс Plane наследуется от класса Vehicle и представляет самолет.

    Атрибуты:
    cargo (int): Текущий груз самолета.
    max_cargo (int): Максимальный груз, который может перевозить самолет.

    Методы:
    load_cargo(cargo): Загружает груз в самолет, если это не приведет к перегрузу.
    remove_all_cargo(): Удаляет весь груз из самолета и возвращает его значение.
    """

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        """
        Инициализирует объект Plane.

        Аргументы:
        weight (int): Вес самолета.
        fuel (int): Количество топлива в самолете.
        fuel_consumption (int): Расход топлива самолета.
        max_cargo (int): Максимальный груз, который может перевозить самолет.
        """
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        """
        Загружает груз в самолет, если это не приведет к перегрузу.

        Аргументы:
        cargo (int): Груз, который нужно загрузить в самолет.

        Если груз приведет к перегрузу, выкидывает исключение CargoOverload.
        """
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload("Cargo overload")

    def remove_all_cargo(self):
        """
        Удаляет весь груз из самолета и возвращает его значение.

        Возвращает:
        int: Значение груза, которое было до обнуления.
        """
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
