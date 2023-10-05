import datetime


class Animal:
    def __init__(self, name: str, age: datetime, commands: str) -> None:
        self.name = name
        self.age = age
        self.commands = commands


class HomeAnimal(Animal):
    def __init__(self, name: str, age: datetime, commands: str) -> None:
        super().__init__(name, age, commands)


class PackedAnimal(Animal):
    def __init__(self, name: str, age: datetime, commands: str) -> None:
        super().__init__(name, age, commands)