# 3) Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа,
# максимальная сумма до основания составляет 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# То есть, 3 + 7 + 4 + 9 = 23.
# Найдите максимальную сумму пути от вершины до основания следующего треугольника:
triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


def path_iterator(row, col):
    current = triangle[row][col]
    if row < len(triangle) - 1:
        next_path = path_iterator(row + 1, col) + path_iterator(row + 1, col + 1)
        return [[current] + path for path in next_path]
    else:
        return [[current]]


paths = path_iterator(0, 0)
max_path = 0
for i, path in enumerate(paths):
    print(f"{i} = {paths[i]} | sum = {sum(path)}")
    if sum(path) > max_path:
        max_path = sum(path)
        index_of_path = i
print(f"max path with sum = {max_path}\n{paths[index_of_path]}")