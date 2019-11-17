"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

from random import random

LEFT_INT = int(input("Начало диапазона: "))
RIGHT_INT = int(input("Конец диапазона: "))
NUMB_INT = int(random()*(RIGHT_INT-LEFT_INT+1)+LEFT_INT)
print(f"Результат генерации случайного целого числа: {NUMB_INT}")

LEFT_FLOAT = float(input("Начало диапазона: "))
RIGHT_FLOAT = float(input("Конец диапазона "))
NUMB_FLOAT = random() * (RIGHT_FLOAT-LEFT_FLOAT)+LEFT_FLOAT
print(f"Результат генерации случайного вещественного числа: {round(NUMB_FLOAT, 3)}")

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
LEFT_LETTER = input("Введите букву английского алфавита - левая граница: ")
LEFT_LETTER = LEFT_LETTER.lower()
RIGHT_LETTER = input("Введите букву английского алфавита - правая граница: ")
RIGHT_LETTER = RIGHT_LETTER.lower()
INDEX_LEFT = ALPHABET.index(LEFT_LETTER)
INDEX_RIGHT = ALPHABET.index(RIGHT_LETTER)
INDEX_RANDOM = int(random()*(INDEX_RIGHT-INDEX_LEFT+1)+INDEX_LEFT)
print(f"Результат генерации случайной буквы: {ALPHABET[INDEX_RANDOM]}")





