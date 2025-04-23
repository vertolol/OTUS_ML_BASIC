from homework_06.base import Vehicle
from homework_06.engine import Engine


class Car(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        if isinstance(engine, Engine):
            self.engine = engine
        else:
            raise ValueError("Engine must be an instance of Engine class")
