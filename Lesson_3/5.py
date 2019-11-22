#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

LIST_TEST = [-1, 2, -6, 7, 8, -91, 54, 1, 0, -31, 8]

MAX_MIN = 0
MAX_MIN_INDEX = -50

for i in range(len(LIST_TEST)):
    if LIST_TEST[i] < 0 and MAX_MIN_INDEX == -50:
        MAX_MIN_INDEX = i
    elif LIST_TEST[i] < 0 and LIST_TEST[i] < LIST_TEST[MAX_MIN_INDEX]:
        MAX_MIN_INDEX = i


print(LIST_TEST)
print(f"{MAX_MIN_INDEX} : {LIST_TEST[MAX_MIN_INDEX]}")
