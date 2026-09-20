from abc import ABC, abstractmethod
# Базовый класс Hero
class Hero(ABC):
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"
     # Дочерние классы
class MageHero(Hero):
    def __init__(self, name, level, hp, mp):
        super().__init__(name, level, hp)
        self.mp = mp # Добавляем ману магу

 # Переопределяем action() для мага
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"
 # WarriorHero наследуется от MageHero   
class WarriorHero(MageHero):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp, mp = 0)
# Переопределяем action() для воина
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.level}"
    
class BankAccount:
    bank_name = "Simba"
    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance  # Защищенный атрибут
        self.__password = password # Приватный атрибут

    # Метод проверки пароля
    def login(self, password):
        if password == self.__password:
            return True
        else:
            return False
        
    def get_bank_name(self):
        return self.bank_name
    
    def bonus_for_level(self):
        return self.hero.level * 10
    # Свойство full_info 
    @property
    def full_info(self):
        return f"Герой: {self.hero.name}, Баланс: {self._balance} SOM"
    # Магические методы в BankAccount
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        # Проверяем, совпадает ли класс героев в аккаунтах
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            return f"Ошибка: Нельзя сложить счета героев разных классов"
    # Сравнение аккаунтов     
    def __eq__(self, other):
        return (type(self.hero) == type(other.hero)) and (self.hero.level == other.hero.level)
    
    # Проверка работы

# Создаем героев
mage1 = MageHero("Merlin", 50, 100, 150)
mage2 = MageHero("Gandalf", 50, 120, 200) 
warrior = WarriorHero("Conan", 50, 200)

# Создаем их банковские счета
acc1 = BankAccount(mage1, 5000, "merlin123")
acc2 = BankAccount(mage2, 3000, "gandalf123")
acc3 = BankAccount(warrior, 4000, "conan123")

# Вызываем методы действий
print(mage1.action())
print(warrior.action())

# Принтуем информацию по счетам 
print(acc1)
print(acc2)

# Проверяем имя банка и бонус за уровень
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

# Проверяем сложение (метод __add__)
print("\n=== Проверка add ===")
print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

# Проверяем сравнение (метод __eq__)
print("\n=== Проверка eq ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)



