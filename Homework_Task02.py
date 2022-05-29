# 2) Вычислить число  Pi c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.
import math
d = 6
pi = 3
for i in range(6, 1296 * d, 4):
    pi += 4/((i - 4) * (i - 3) * (i - 2)) - 4/((i - 2) * (i - 1) * i)
print(round(pi, d))
print(round(math.pi, d))