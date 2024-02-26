class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

    def description(self):
        return f"Name: {self.name}, Food: {self.food}, Habitat: {self.habitat}, Reproduction: {self.reproduction}"


class Rhino(Animal):
    def __init__(self, name, food, habitat, reproduction, horn_size):
        super().__init__(name, food, habitat, reproduction)
        self.horn_size = horn_size

    def sound(self):
        return "Snort!"

    def info(self):
        return f"{super().description()}, Horn Size: {self.horn_size}"


class Fish(Animal):
    def __init__(self, name, food, habitat, reproduction, water_type):
        super().__init__(name, food, habitat, reproduction)
        self.water_type = water_type

    def swim(self):
        return "Fish swims by moving its tail."

    def info(self):
        return f"{super().description()}, Water Type: {self.water_type}"


class Snake(Animal):
    def __init__(self, name, food, habitat, reproduction, length):
        super().__init__(name, food, habitat, reproduction)
        self.length = length

    def slither(self):
        return "The snake moves by slithering across the ground."

    def info(self):
        return f"{super().description()}, Length: {self.length}"


6
rhino = Rhino("Rhino", "Grass", "Grasslands", "Viviparous", "Large")
print(rhino.info())
print(rhino.sound())

fish = Fish("Goldfish", "Flakes", "Freshwater", "Oviparous", "Freshwater")
print(fish.info())
print(fish.swim())

snake = Snake("Python", "Small Animals", "Various", "Oviparous", "Long")
print(snake.info())
print(snake.slither())
