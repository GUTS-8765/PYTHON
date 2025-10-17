start = int(input("Введите начальное число в диапозоне: "))
end = int(input("Введите конечное число в диапозоне: "))
print("Числа диапозона: ")
for num in range(start, end + 1):
    print(num, end= " ")
print("\n")
print ("числа кратные 7:")
for num in range(start, end + 1):
    if num % 7 == 0:
        print(num, end=" ")
print("\n")
count_multiples_of_5 = sum(1 for num in range(start, end + 1) if num % 5 == 0)
print(f"Количество чисел, кратных 5: {count_multiples_of_5}")