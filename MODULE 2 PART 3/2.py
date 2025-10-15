num = float(input("введите число: "))
power = int(input("Введите степень от 0 до 7: "))
if power in range(8):
    result = num ** power
    print(f"{num} в степени {power} равно {result}")
else:
    print("Степень должна быть от 0 до 7!")