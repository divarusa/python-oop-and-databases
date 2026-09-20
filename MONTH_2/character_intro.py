# Класс Hero описывает персонажа игры
class Hero:
    # Инициализатор класса задает имя, уровень, здоровье и силу персонажа
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    # Метод приветствия персонажа
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    # Метод атаки выводит сообщение и уменьшает силу персонажа на 1
    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    # Метод отдыха выводит сообщение и увеличивает здоровье персонажа на 1
    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


# проверка задания


# Создаем двух персонажей с начальными характеристиками
hero1 = Hero("Наруто", 5, 10, 8)
hero2 = Hero("Барби", 10, 7, 4)

# Вызываем все методы для первого героя и проверяем изменение параметров
hero1.greet()
hero1.attack()
print(hero1.strength)  # Выведет 7 (было 8)
hero1.rest()
print(hero1.health)    # Выведет 11 (было 10)

# Вызываем все методы для второго героя и проверяем изменение параметров
hero2.greet()
hero2.attack()
print(hero2.strength)  # Выведет 3 (было 4)
hero2.rest()
print(hero2.health)    # Выведет 8 (было 7)

    