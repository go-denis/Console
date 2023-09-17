class AnimalRegistry:
    def __init__(self):
        self.animals = []
        self.counter = 0

    def add_animal(self, name, age, animal_type):
        self.counter += 1
        animal = None
        if animal_type.lower() == "dog":
            animal = Dog(name, age)
        elif animal_type.lower() == "cat":
            animal = Cat(name, age)
        elif animal_type.lower() == "hamster":
            animal = Hamster(name, age)
        elif animal_type.lower() == "horse":
            animal = Horse(name, age)
        elif animal_type.lower() == "camel":
            animal = Camel(name, age)
        elif animal_type.lower() == "donkey":
            animal = Donkey(name, age)
        if animal:
            self.animals.append(animal)
            print(f"{animal_type.capitalize()} named {name} added to the registry.")

    def list_commands(self, animal_name):
        for animal in self.animals:
            if animal.get_name() == animal_name:
                print(f"{animal_name} can perform the following commands:")
                animal.commands()

    def teach_command(self, animal_name, command):
        for animal in self.animals:
            if animal.get_name() == animal_name:
                animal.add_command(command)
                print(f"{command} added to {animal_name}'s commands.")

    def menu(self):
        while True:
            print("\nAnimal Registry Menu:")
            print("1. Add a new animal")
            print("2. List commands for an animal")
            print("3. Teach a command to an animal")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter the name of the animal: ")
                age = int(input("Enter the age of the animal: "))
                animal_type = input("Enter the type of the animal (e.g., dog, cat, hamster): ")
                self.add_animal(name, age, animal_type)
            elif choice == "2":
                animal_name = input("Enter the name of the animal: ")
                self.list_commands(animal_name)
            elif choice == "3":
                animal_name = input("Enter the name of the animal: ")
                command = input("Enter the command to teach: ")
                self.teach_command(animal_name, command)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"Total animals added: {self.counter}")
        else:
            print("An exception occurred. Resource not closed properly.")


class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._commands = []

    def get_name(self):
        return self._name

    def commands(self):
        print(", ".join(self._commands))

    def add_command(self, command):
        self._commands.append(command)


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._commands = ["sit", "stay", "fetch"]


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._commands = ["purr", "hunt"]


class Hamster(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._commands = ["run in wheel", "climb"]


class Horse(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._commands = ["gallop", "jump"]


class Camel(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._commands = ["carry load", "walk in the desert"]


class Donkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._commands = ["carry load", "bray"]


if __name__ == "__main__":
    with AnimalRegistry() as registry:
        registry.menu()
