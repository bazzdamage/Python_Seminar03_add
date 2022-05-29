# 2) Определите функцию, которая удаляет весь текст, следующий за любым из переданных маркеров комментариев.
# Любые пробелы в конце строки также должны быть удалены.
# Пример:
# Входные данные:
# «apples, pears # and bananas
# grapes
# bananas !apples          »
# Выходные данные:
# «apples, pears
# grapes
# bananas»
# Функция может вызываться вот так:
# result = function("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
input_string = "apples, pears # and bananas\ngrapes\nbananas !apples\nagain bananas    "
separators = ["#", "!"]


def remove_unecessary(input: str, separators: list):
    splice = input.splitlines()
    output = []
    for item in splice:
        flag = 0
        for sep in separators:
            if str(item).find(sep) != -1:
                temp = item.split(sep)
                output.append(temp[0].strip())
                flag = 1
        if flag != 1:
            output.append(item.strip())
    return output


print(remove_unecessary(input_string, separators))