# 4) . Сумма квадратов первых десяти натуральных чисел равна
# 12 + 22 + ... + 102 = 385
# Квадрат суммы первых десяти натуральных чисел равен
# (1 + 2 + ... + 10)2 = 552 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел
# составляет 3025 − 385 = 2640.
# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
import math


def sum_of_sqr(n):
    return sum(i * i for i in range(n+1))


def sqr_of_sum(n):
    return int(math.pow(sum(i for i in range(n+1)), 2))


print(sqr_of_sum(10) - sum_of_sqr(10))
print(sqr_of_sum(100) - sum_of_sqr(100))
print(sqr_of_sum(1000) - sum_of_sqr(1000))