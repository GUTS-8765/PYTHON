num1 = float(input("введите первое чиисло: "))
num2 = float(input("введите второе чиисло: "))
num3 = float(input("введите третье чиисло: "))
print("\nВыберите действие:")
print("1 - Найти максимальное число")
print("2 - Найти минимальное число")
print("3 - Найти среднее арифметическое")
choice = input("Введите номер действия (1/2/3): ")
if choice == '1':
    result = max(num1, num2, num3)
    print(f"\nМаксимальное число: {result}")
elif choice == '2':
    result = min(num1, num2, num3)
    print(f"\nМинимальное число: {result}")
elif choice == '3':
    result = (num1 + num2 + num3) / 3
    print(f"\nСреднее арифметическое: {result:.2f}")
else:
    print("\nОшибка: неверный номер действия")  