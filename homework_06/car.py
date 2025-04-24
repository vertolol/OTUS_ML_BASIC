from homework_06.base import Vehicle
from homework_06.engine import Engine


class Car(Vehicle):
    """
    Класс Car наследуется от класса Vehicle и представляет автомобиль.

    Атрибуты:
    engine (Engine): Двигатель автомобиля.

    Методы:
    set_engine(engine): Устанавливает двигатель автомобиля.
    """

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        """
        Инициализирует объект Car.

        Аргументы:
        weight (int): Вес автомобиля.
        fuel (int): Количество топлива в автомобиле.
        fuel_consumption (int): Расход топлива автомобиля.
        """
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        """
        Устанавливает двигатель автомобиля.

        Аргументы:
        engine (Engine): Двигатель автомобиля.

        Если переданный объект не является экземпляром класса Engine, выкидывает исключение ValueError.
        """
        if isinstance(engine, Engine):
            self.engine = engine
        else:
            raise ValueError("Engine must be an instance of Engine class")
