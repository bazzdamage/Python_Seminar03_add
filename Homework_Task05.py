# 1) Определите функцию, которая принимает римскую цифру в качестве аргумента и
# возвращает ее значение в виде числового десятичного целого числа.
# Вам не нужно проверять форму римской цифры.
# Современные римские цифры записываются путем выражения каждой десятичной цифры числа,
# которое должно быть закодировано отдельно, начиная с самой левой цифры.
# Таким образом, 1990 отображается "MCMXC" (1000 = M, 900 = CM, 90 = XC),
# а 2008 отображается "MMVIII" (2000 = MM, 8 = VIII). Римская цифра для 1666, "MDCLXVI",
# использует каждую букву в порядке убывания.
# Пример: имявашейфункции ('XXI') # должно вернуть 21
romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
roman_num = "MCMXC"


def roman_to_arab(roman_num):
    arab_num = 0
    for i, letter in enumerate(roman_num):
        if i + 1 < len(roman_num) and romans[roman_num[i]] < romans[roman_num[i + 1]]:
            arab_num -= romans[roman_num[i]]
        else:
            arab_num += romans[roman_num[i]]
    return arab_num


print(roman_to_arab(roman_num))

