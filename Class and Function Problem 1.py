# classes_exercise.py

"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""
import self as self
import switch as switch


class Vehicle:

    def __init__(self, name: str, capacity: int, max_speed: int):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

    def vroom(self) -> None:
        result = self.max_speed
        return "vroom \n" * result

vehicle = Vehicle("BMW", 5, 20)
print(vehicle.vroom())

class Bus(Vehicle):

    def __init__(self, name: str, capacity: int, max_speed: int):
        super().__init__(name, capacity, max_speed)

    def fare(self, age: float)->None:
        price = ""
        if age>=18 and age <=60:
            price = "5$"
            print(price)
        else:
            price = "Free"
            print(price)

bus = Bus("BUS", 40, 10)
bus.fare(18)
bus.fare(-1)
bus.fare(17)
bus.fare(0)
bus.fare(60)
bus.fare(60.1)