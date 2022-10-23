"""Вычислить число c заданной точностью d"""

from decimal import Decimal
number_round_down = 0
number_input = 0

def number_calculus(number_round_down,number_input):
    number_round_down = Decimal(input('Введите число с числами после запятой: '))
    number_input = input('Введите требуемую точность в формате "0.0001":')
    if number_input in (0,1):
        number_round_down = number_round_down.quantize(Decimal(number_input))
        print(number_round_down)
    else:
        print('Введите число в формате "0.000001"')
        number_calculus(number_round_down,number_input)

number_calculus(number_round_down,number_input)