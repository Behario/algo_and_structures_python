# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random
MAX = 5
MIN = 0

LINE = 5
COLUMN = 4
matrix = []
for i in range(LINE):
    matrix_line = []
    print(f"{i}-я строка:")
    for j in range(COLUMN):
        element = int(random()*(MAX-MIN+1)+MIN)
        matrix_line.append(element)
    matrix.append(matrix_line)

for i in matrix:
    print(i)

matrix_2 = []
for i in range(LINE):
    MIN_IN_LINE = 1000
    for j in range(COLUMN):
        if matrix[i][j] < MIN_IN_LINE:
            MIN_IN_LINE = matrix[i][j]
    matrix_2.append(MIN_IN_LINE)

MAX_IN_LINE = -1000
for i in matrix_2:
    if i > MAX_IN_LINE:
        MAX_IN_LINE = i

print(f"Максимальный элемент среди минимальных: {MAX_IN_LINE}")