"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

NUMBER = int(input("Введите натуральное число: "))
NUMBER_BACKWARD = 0

while NUMBER > 0:
    DIG = NUMBER % 10
    NUMBER = NUMBER // 10
    NUMBER_BACKWARD = NUMBER_BACKWARD * 10
    NUMBER_BACKWARD = NUMBER_BACKWARD + DIG

print(NUMBER_BACKWARD)


# Через рекурсию


def reverse(number, reverse_number=0):
    if number == 0:
        return f'{reverse_number}'
    else:
        reverse_number = int((reverse_number + (number % 10) * 0.1) * 10)
        number = number // 10
        return reverse(number, reverse_number)


NUMBER = int(input("Введите число: "))

print(reverse(NUMBER))


