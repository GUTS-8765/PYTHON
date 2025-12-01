while True:
    try:
        num_str = input("Введите число: ")
        num = int(num_str)

        if num > 0:
            print("Number is positive")
        elif num < 0:
            print("Number is negative")
        else:
            print("Number is equal to zero")

        if num == 7:
            print("Good bye!")
            break

    except ValueError:
        print("Пожалуйста, введите корректное число.")
