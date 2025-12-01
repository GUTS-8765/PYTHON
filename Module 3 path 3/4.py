def remove_3_and_6(number):
    number_str = str(number)
    new_number_str = ""
    for digit in number_str:
        if digit != '3' and digit != '6':
            new_number_str += digit

    if not new_number_str:
        return 0
    else:
        return int(new_number_str)


try:
    user_input = int(input("Введите целое число: "))
    result = remove_3_and_6(user_input)
    print(f"Число без цифр 3 и 6: {result}")
except ValueError:
    print("Ошибка: введено не целое число.")