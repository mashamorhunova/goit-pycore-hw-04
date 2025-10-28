
import sys
from pathlib import Path
from colorama import Fore, init

# Ініціалізація colorama
init(autoreset=True)

# Перевіряємо, чи передано шлях до директорії
if len(sys.argv) < 2:
    print("Будь ласка, вкажіть шлях до директорії")
    print("Приклад: python hw03.py .")
    sys.exit()

# Отримуємо шлях з командного рядка
directory_path = sys.argv[1]
path = Path(directory_path)

# Перевіряємо, чи існує директорія
if not path.exists():
    print(Fore.RED + "Помилка: Такого шляху не існує!")
    sys.exit()

if not path.is_dir():
    print(Fore.RED + "Помилка: Це не директорія!")
    sys.exit()

# Виводимо назву головної директорії
print(Fore.BLUE + f"{path.name}/")

# Проходимо по всіх елементах у директорії
for item in path.iterdir():
    if item.is_dir():
        # Якщо це директорія - виводимо синім
        print(Fore.BLUE + f"  {item.name}/")
    else:
        # Якщо це файл - виводимо зеленим
        print(Fore.GREEN + f"  {item.name}")