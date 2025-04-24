from dataclasses import dataclass


@dataclass
class Engine:
    """
    Класс Engine представляет двигатель.

    Атрибуты:
    volume (float): Объем двигателя.
    pistons (int): Количество поршней в двигателе.
    """
    volume: float
    pistons: int
