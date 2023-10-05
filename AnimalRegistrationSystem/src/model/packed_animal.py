import datetime

from src.model.animal_base import PackedAnimal


class Horse(PackedAnimal):
    def __init__(self, name: str, age: datetime, commands: str) -> None:
        super().__init__(name, age, commands)


class Camel(PackedAnimal):
    def __init__(self, name: str, age: datetime, commands: str) -> None:
        super().__init__(name, age, commands)


class Donkey(PackedAnimal):
    def __init__(self, name: str, age: datetime, commands: str) -> None:
        super().__init__(name, age, commands)