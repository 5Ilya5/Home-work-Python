﻿n = int(input("Введите десятичное число: "))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)