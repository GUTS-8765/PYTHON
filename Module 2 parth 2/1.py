num1 = float(input("введите первое чиисло: "))
num2 = float(input("введите второе чиисло: "))
num3 = float(input("введите третье чиисло: "))
choice = input("выберите операцию (сумма/произведения): ")
if choice.lower() == "сумма":
    result = num1 + num2 + num3
    print(f"Сумма чисел: {result}")
elif choice.lower() == "произведение":
    result = num1 * num2 * num3
    print(f"Произведение чисел: {result}")
else:
    print("Неверный выбор операции!")