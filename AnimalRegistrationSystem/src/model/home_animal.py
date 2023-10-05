import datetime

from src.model.animal_base import HomeAnimal


class Dog(HomeAnimal):
    def __init__(self, name: str, age: datetime, commands: str) -> None:
        super().__init__(name, age, commands)


class Cat(HomeAnimal):
    def __init__(self, name: str, age: datetime, commands: str) -> None:
        super().__init__(name, age, commands)


class Hamster(HomeAnimal):
    def __init__(self, name: str, age: datetime, commands: str) -> None:
        super().__init__(name, age, commands)