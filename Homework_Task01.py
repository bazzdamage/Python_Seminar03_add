# 1) Найти НОК двух чисел
a = 112
b = 355
max_num = max(a, b)
min_num = min(a, b)
for i in range(1, min_num + 1):
    if (max_num * i) % min_num == 0:
        print(f"{max_num * i} = LCM of {a} and {b}")
        exit()