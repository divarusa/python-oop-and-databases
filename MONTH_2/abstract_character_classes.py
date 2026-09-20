from abc import ABC, abstractmethod

# Абстрактный базовый класс
class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health # приватный атрибут
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1 #

# Обязательный абстрактный метод
    @abstractmethod
    def attack(self):
        pass

# Дочерний класс Warrior
class Warrior(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)
    
# Переопределение абстрактного метода атаки для Воина
    def attack(self):
        print(f"{self.name} атакует мечом")

# Дочерний класс Mage
class Mage(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)

# Переопределение абстрактного метода атаки для Мага
    def attack(self):
        print(f"{self.name} использует магию")

# Дочерний класс Assassin 
class Assassin(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)

# Переопределение абстрактного метода атаки для Ассасина
    def attack(self): 
        print(f"{self.name} атакует исподтишка")

# Создание объектов (экземпляров) конкретных классов персонажей
warrior = Warrior("Arthur", 5, 100, 15)
mage = Mage("Gendalf", 7, 80 ,5)
assassin = Assassin("Elio", 6, 90 ,12)

# Демонстрация работы методов для Воина
warrior.greet()
warrior.attack()
warrior.rest()

# Демонстрация работы методов для Мага
mage.greet()
mage.attack()
mage.rest()

# Демонстрация работы методов для Ассассина
assassin.greet()
assassin.attack()
assassin.rest()
