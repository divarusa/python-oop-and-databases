import random

# Базовый (родительский) класс для всех персонажей игры⁠
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}")
    
    def attack(self):
        print(f"{self.name} наносит удар")
    
    def rest(self):
        print(f"{self.name} отдыхает")
        self.health += 10
# Дочерний класс Воина, наследующий свойства Героя⁠
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
       # Вызываем конструктор родительского класса для базовых атрибутов⁠
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    # Переопределение метода атаки (полиморфизм)⁠
    def attack(self):
        print("Воин атакует мечом!")
# Дочерний класс Мага, наследующий свойства Героя⁠
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        print("Маг кастует заклинание!")
# Дочерний класс Ассасина, наследующий свойства Героя⁠
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        print("Ассасин атакует исподтишка!")
# Создаем конкретные объекты (экземпляры) классов-героев⁠
rock = Warrior("Arthur", 1, 100, 15, 50)
paper = Mage("Gandalf", 5, 80, 5, 100)
scissors = Assassin("Ezio", 3, 90, 12, 80)

# Логика самой игры  
player_choice = input("Выберите героя: (Warrior/Mage/Assasin: )")
varieties = [rock, paper, scissors]

# Компьютер случайно выбирает персонажа из списка⁠
enemy = random.choice(varieties)
enemy_type = type(enemy).__name__

print(f"Вы выбрали: {player_choice}")
print(f"Противник: {enemy_type}")

# Проверка результатов игры по принципу "Камень, ножницы, бумага
if player_choice == enemy_type:
    print("Ничья!")
elif (player_choice == "Warrior" and enemy_type == "Assassin") or \
    (player_choice == "Assassin" and enemy_type == "Mage") or \
    (player_choice == "Mage" and enemy_type == "Warrior"):
    print(f"Вы победили! {player_choice} оказался сильнее.")
else:
    print(f"{enemy_type} победил!")





