start_range = int(input("Введите начало диапазона таблицы: "))
end_range = int(input("Введите конец диапазона таблицы: "))
print(f"Таблица умножения от {start_range} до {end_range}:")
for i in range(start_range, end_range + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
    print("-" * 10)
