class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
def attack(self):
    print(f"{self.name} character attacks {self.hp} hp.")
def __str__(self):
    return f"{self.name} HP: {self.hp} HP: {self.power}"
class warrior(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp * 1.2, power * 1.5)
    def attack(self):
        print(f"{self.name} warrior attacks {self.hp} hp.")
class mage(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp * 1.2, power * 1.5)
    def attack(self):
        print(f"{self.name} mage attacks {self.hp} hp.")
characters = []
def show_menu():
    print("\n--- Система персонажей ---")
    print("1. Создать персонажа")
    print("2. Показать всех персонажей")
    print("3. Атака персонажа")
    print("4. Выход")

def create_character():
    print("\n--- Создание персонажа ---")
    char_type = input("Выберите тип (w - воин, m - маг): ").lower()
    name = input("Введите имя: ")
    try:
        hp = int(input("Введите здоровье (HP): "))
        power = int(input("Введите силу (Power): "))
        if char_type == 'w':
            characters.append(warrior(name, hp, power))
            print(f"Воин {name} создан!")
        elif char_type == 'm':
            mana = int(input("Введите ману (Mana): "))
            characters.append(mage(name, hp, power, mana))
            print(f"Маг {name} создан!")
        else:
            print("Неверный тип персонажа. Создан обычный персонаж.")
            characters.append(Character(name, hp, power))
    except ValueError:
        print("Ошибка: Здоровье, сила и мана должны быть числами.")

def show_all_characters():
    if not characters:
        print("Персонажей пока нет.")
        return
    print("\n--- Все персонажи ---")
    for i, char in enumerate(characters):
        print(f"{i+1}. {char}")

def perform_attack():
    if not characters:
        print("Нет персонажей для атаки.")
        return
    print("\n--- Атака персонажа ---")
    show_all_characters()
    try:
        index = int(input("Выберите номер персонажа для атаки: ")) - 1
        if 0 <= index < len(characters):
            characters[index].attack()
        else:
            print("Неверный номер персонажа.")
    except ValueError:
        print("Ошибка: Введите номер.")


while True:
    show_menu()
    choice = input("Ваш выбор: ")

    if choice == '1':
        create_character()
    elif choice == '2':
        show_all_characters()
    elif choice == '3':
        perform_attack()
    elif choice == '4':
        print("Выход из программы. До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")