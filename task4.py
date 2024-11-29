# 4th program
# Дано число в виде строки
num_str = '123.456'
# Преобразование в дробное число
num = float(num_str)
# Смещение первой цифры после запятой в целую часть
shifted = num * 10
# Берем целую часть числа
shifted_int = int(shifted)
# Находим первую цифру после запятой с помощью остаточного деления на 10
first_decimal_digit = shifted_int % 10

print(first_decimal_digit)
