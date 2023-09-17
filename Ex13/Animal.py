class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

class DomesticAnimal(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self._owner = owner

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner

class Dog(DomesticAnimal):
    def __init__(self, name, age, owner, breed):
        super().__init__(name, age, owner)
        self._breed = breed

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

class Cat(DomesticAnimal):
    def __init__(self, name, age, owner, color):
        super().__init__(name, age, owner)
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

class Hamster(DomesticAnimal):
    def __init__(self, name, age, owner, fur_color):
        super().__init__(name, age, owner)
        self._fur_color = fur_color

    def get_fur_color(self):
        return self._fur_color

    def set_fur_color(self, fur_color):
        self._fur_color = fur_color

class PackAnimal(Animal):
    def __init__(self, name, age, load_capacity):
        super().__init__(name, age)
        self._load_capacity = load_capacity

    def get_load_capacity(self):
        return self._load_capacity

    def set_load_capacity(self, load_capacity):
        self._load_capacity = load_capacity

class Horse(PackAnimal):
    def __init__(self, name, age, load_capacity, breed, color):
        super().__init__(name, age, load_capacity)
        self._breed = breed
        self._color = color

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

class Camel(PackAnimal):
    def __init__(self, name, age, load_capacity, hump_count):
        super().__init__(name, age, load_capacity)
        self._hump_count = hump_count

    def get_hump_count(self):
        return self._hump_count

    def set_hump_count(self, hump_count):
        self._hump_count = hump_count

class Donkey(PackAnimal):
    def __init__(self, name, age, load_capacity):
        super().__init__(name, age, load_capacity)

# Пример использования классов:
dog = Dog("Buddy", 3, "John", "Golden Retriever")
print(f"{dog.get_name()} is a {dog.get_breed()} dog owned by {dog.get_owner()}.")
