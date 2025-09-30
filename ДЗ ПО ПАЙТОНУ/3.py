m_convert = {'миля': lambda x: x / 1609.34,
             'дюйм': lambda x: x * 39.37,
             'ярд': lambda x: x * 1.0936}

m = int(input('Количество метров: '))
print('Варианты конвертации: миля, дюйм, ярд')
cnv_type = input('Во что конвертировать: ')
print(f'{m} = {m_convert[cnv_type](m):.2f}')