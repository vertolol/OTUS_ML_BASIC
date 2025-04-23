from homework_06.base import Vehicle
from homework_06.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload("Cargo overload")

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
