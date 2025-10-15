tariffs = {
    'МТС': {'МТС': 1.0, 'Билайн': 1.2, 'Мегафон': 1.3},
    'Билайн': {'МТС': 1.2, 'Билайн': 1.0, 'Мегафон': 1.1},
    'Мегафон': {'МТС': 1.3, 'Билайн': 1.1, 'Мегафон': 1.0}
}
operators = list(tariffs.keys())

print('Выберите оператора, с которого звоните:')
for index, operator in enumerate(operators, start=1):
    print(f'{index}. {operator}')

from_operator_choice = int(input('Ваш выбор (номер): '))
from_operator = operators[from_operator_choice - 1]

print('\nВыберите оператора, на который звоните:')
for index, operator in enumerate(operators, start=1):
    print(f'{index}. {operator}')

to_operator_choice = int(input('Ваш выбор (номер): '))
to_operator = operators[to_operator_choice - 1]
cost_per_minute = float(input("\nСтоимость базовой минуты разговора (рублей/минуту): "))
duration_minutes = float(input("Продолжительность разговора (минуты): "))
total_cost = cost_per_minute * tariffs[from_operator][to_operator] * duration_minutes
print(f'\nОбщая стоимость разговора составит: {round(total_cost, 2)} рублей.')