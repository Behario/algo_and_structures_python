"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def finder(numbers, number, number_counter = 0):
    if numbers == 0:
        return f"{number_counter}"
    else:
        if numbers % 10 == number:
            number_counter += 1
        numbers = numbers // 10
        return finder(numbers, number, number_counter)


NUMBERS = int(input("Введите составное число: "))
NUMBER = int(input("Какую цифру ищем: "))

print(f'Мы ищем количество вхождений {NUMBER} в {NUMBERS}, давайте узнаем: ровно {finder(NUMBERS, NUMBER)} раза')