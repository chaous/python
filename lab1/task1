class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def makesound(self):
        print(f"{self.name} издает звук: {self.sound}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Мяу")
        self.color = color
    
    def makesound(self):
        print(f"{self.name} ({self.color}) издает звук: {self.sound}")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Гав")
        self.color = color
    
    def makesound(self):
        print(f"{self.name} ({self.color}) издает звук: {self.sound}")

# Создание объектов
cat = Cat("Кот", "рыжий")
dog = Dog("Собака", "черный")

# Вызов метода makesound()
cat.makesound()  # Выведет: Кот (рыжий) издает звук: Мяу
dog.makesound()  # Выведет: Собака (черный) издает звук: Гав
