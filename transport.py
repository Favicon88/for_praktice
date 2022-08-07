from dataclasses import dataclass
from mixins import Brake


class Transport:
    def __init__(self, fuel) -> None:
        self.fuel = fuel
        self.distance = 0
        self.__color = "red"
        self._wheels = 4

    def get_color(self):
        """Getter."""
        return self.__color

    def repaint(self, color):
        """Setter."""
        self.__color = color


class Boat(Transport):
    def __init__(self, fuel) -> None:
        print("Init Boat")
        super().__init__()


class Car(Transport, Brake):
    def __init__(self) -> None:
        print("Init car")
        fuel = 40
        super().__init__(fuel)

    def __str__(self) -> str:
        return "Машина"


class ElectroCar(Car):
    def __init__(self, fuel) -> None:
        super(Transport, self).__init__(fuel)


class Amphibian(Boat, Car):
    pass
    # def __init__(self) -> None:
    #     super().__init__()


if __name__ == "__main__":
    # t1 = Transport(50)
    car = Car()
    # car2 = Car(50)
    # solo = Amphibian(50)
    pass
