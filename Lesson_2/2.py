"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

NUMBER = input("Введите натуральное число: ")
EVEN = ""
ODD = ""
EVEN_COUNTER = 0
ODD_COUNTER = 0

for i in NUMBER:
    if int(i) % 2 == 0:
        EVEN_COUNTER += 1
        EVEN = EVEN + f"{i} "
    elif int(i) % 2 != 0:
        ODD_COUNTER += 1
        ODD = ODD + f"{i} "
print(f"Четные составные числа в количестве {EVEN_COUNTER}: {EVEN}\n"
      f"Нечетные составные числа в количестве {ODD_COUNTER}: {ODD}")


# Решение через рекурсию


def numbers(number, even_counter=0, odd_counter=0):

    if number == 0:
        return even_counter, odd_counter
    else:
        if (number % 10) % 2 == 0:
            even_counter += 1
        elif (number % 10) % 2 != 0:
            odd_counter += 1

    number = number // 10
    return numbers(number, even_counter, odd_counter)


print(f'Подсчет количества четных и нечетных составных чисел числа {NUMBER} через рекурсию : Четные, нечетные - {numbers(int(NUMBER))}')

