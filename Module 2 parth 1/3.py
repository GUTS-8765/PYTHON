from random import choice

METRS = int(input('Метры: '))
Choice =  (input('<введите во что надо перевести метры (мили, ярды, дюймы)>: '))
if Choice == "мили":
    print(METRS / 1609.34)
elif choice == "ярды":
    print(METRS / 0.9144)
elif Choice == "дюймы":
    print(METRS * 39.3701)
else:
    print("ошибка")