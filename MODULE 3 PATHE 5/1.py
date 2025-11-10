def print_square(size):
    for _ in range(size):
        print("*" * size)

def print_triangle(size):
    for i in range(1, size + 1):
        print("*" * i)

def print_pyramid(size):
    for i in range(1, size + 1):
        print(" " * (size - i) + "*" * (2 * i - 1))

def show_menu():
    print("\nВыберите фигуру для вывода:")
    print("1. Квадрат")
    print("2. Треугольник")
    print("3. Пирамида")
    print("0. Выход")

def main():
    while True:
        show_menu()
        choice = input("Ваш выбор: ")

        if choice == '1':
            try:
                size = int(input("Введите размер квадрата: "))
                if size > 0:
                    print_square(size)
                else:
                    print("Размер должен быть положительным числом.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
        elif choice == '2':
            try:
                size = int(input("Введите размер треугольника: "))
                if size > 0:
                    print_triangle(size)
                else:
                    print("Размер должен быть положительным числом.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
        elif choice == '3':
            try:
                size = int(input("Введите размер пирамиды: "))
                if size > 0:
                    print_pyramid(size)
                else:
                    print("Размер должен быть положительным числом.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
        elif choice == '0':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите из предложенных вариантов.")

if __name__ == "__main__":
    main()