# Словарь курсов валют относительно сома
rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    # Метод конвертации любой валюты в сомы
    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    # Магический метод для красивого вывода
    def __str__(self):
        return f"{self.amount} {self.currency}"

    # Магический метод сложения 
    def __add__(self, other):
        if not isinstance(other, Money):
            return "Ошибка: Можно складывать только с объектом Money!"
        
        # Если валюты одинаковые, просто складываем суммы
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            # Если разные,переводим обе в KGS, складываем и возвращаем в KGS
            total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
            return Money(total_kgs, "KGS")

    # Магический метод вычитания
    def __sub__(self, other):
        if not isinstance(other, Money):
            return "Ошибка: Можно вычитать только объект Money!"
        
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            total_kgs = self.convert_to_kgs() - other.convert_to_kgs()
            return Money(total_kgs, "KGS")

    # Магический метод умножения
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return "Ошибка: Деньги можно умножать только на число!"

    # Магический метод деления
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                return "Ошибка: Деление на ноль!"
            return Money(self.amount / other, self.currency)
        return "Ошибка: Деньги можно делить только на число!"


# Проверка работы
if __name__ == "__main__":
    money1 = Money(100, "USD")
    money2 = Money(5000, "KGS")

    # 1. Проверка сложения разных валют 
    result_add = money1 + money2
    print("Сложение:", result_add)

    # 2. Проверка вычитания разных валют 
    result_sub = money1 - money2
    print("Вычитание:", result_sub)

    # 3. Проверка умножения 
    result_mul = money1 * 3
    print("Умножение:", result_mul)

    # 4. Проверка деления
    result_div = money2 / 2
    print("Деление:", result_div)