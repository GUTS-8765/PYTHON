number_str = input("Введите четырёхзначное число: ")

# Проверяем, что длина строки равна 4 (для четырёхзначного числа)
if len(number_str) == 4 and number_str.isdigit():
    # Переворачиваем строку с помощью среза [::-1]
    reversed_number_str = number_str[::-1]

    # Преобразуем перевёрнутую строку обратно в целое число
    reversed_number = int(reversed_number_str)

    # Выводим результат
    print(f"Перевёрнутое число: {reversed_number}")
else:
    print("Введено некорректное число. Пожалуйста, введите четырёхзначное число.")