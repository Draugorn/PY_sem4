"""Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""

import math

number_breakdown=int(input("Введите число: "))

for i in range(2, int(math.sqrt(number_breakdown)) + 1): 
    while (number_breakdown % i == 0): 
        print(i)
        number_breakdown //= i 
if (number_breakdown != 1): 
    print (number_breakdown)