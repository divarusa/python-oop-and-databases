# Эта библиотека нужна для раскрашивания текста и фона в консоли,
# чтобы сделать вывод программы более наглядным и удобным для чтения
import colorama
from colorama import Fore, Style
colorama.init()

# Пример использования
print(Fore.RED + "Привет, это красный текст!" + Style.RESET_ALL)
print(Fore.GREEN + "Это зеленый текст!" + Style.RESET_ALL)