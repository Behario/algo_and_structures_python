"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
from random import random

RANDOM = int(random()*(100 - 0 + 1) + 0)
n = 0

while n <= 9:
    ANSWER = int(input("Загадайте число: "))
    if n < 9:
        if RANDOM == ANSWER:
            print(f"Вы угадали, правильное число - {ANSWER}")
            break
        elif RANDOM != ANSWER:
            if RANDOM > ANSWER:
                print("Ответ неправильный, загаданное вами число меньше, попробуйте еще раз")
            elif RANDOM < ANSWER:
                print("Ответ неправильный, загаданное вами число больше, попробуйте еще раз")
    elif n == 9:
        if RANDOM == ANSWER:
            print(f"Вы угадали, правильное число - {ANSWER}")
        else:
            print(f"Вы проиграли, правильное число: {RANDOM}")

    n = n + 1