# 3)Составить список простых множителей натурального числа N
n = 1895555


def simple_multipliers (n):
    simple_mult = []
    for i in range (2, n + 1):
        if (n % i == 0):
            while n % i == 0:
                simple_mult.append(i)
                n /= i
    return simple_mult


print(simple_multipliers(n))