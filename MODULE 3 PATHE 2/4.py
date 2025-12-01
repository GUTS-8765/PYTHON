total_sum = 0
min_val = float('inf')
max_val = float('-inf')
is_first_input = True

while True:
    try:
        num_str = input("Введите число (или 7 для выхода): ")
        num = int(num_str)

        if num == 7:
            print("Good bye!")
            break

        total_sum += num

        if is_first_input:
            min_val = num
            max_val = num
            is_first_input = False
        else:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num

    except ValueError:
        print("Пожалуйста, введите корректное число.")

if not is_first_input:  # Выводим статистику только если было введено хотя бы одно число кроме 7
    print(f"Сумма: {total_sum}")
    print(f"Максимум: {max_val}")
    print(f"Минимум: {min_val}")