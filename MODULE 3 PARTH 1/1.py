start = int(input("Введите начальное число в диапозоне: "))
end = int(input("Введите конечное число в диапозоне: "))
for num in range(start, end + 1):
    if num % 7 ==0:
        print(num)