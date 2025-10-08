metrs = int(input('Метры: '))
choice =  (input('<введите во что надо перевести метры (мили, ярды, дюймы)>: '))
if choice == "мили":
    print(metrs / 1609.34)
elif choice == "ярды":
    print( metrs/ 0.9144)
elif choice == "дюймы":
    print(metrs * 39.3701)
else:
    print("ошибка")