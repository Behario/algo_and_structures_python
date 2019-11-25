"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
LINE = 5
COLUMN = 4
matrix = []
for i in range(LINE):
    matrix_line = []
    sum = 0
    print(f"{i}-я строка:")
    for j in range(COLUMN - 1):
        element = int(input())
        sum += element
        matrix_line.append(element)
    matrix_line.append(sum)
    matrix.append(matrix_line)

for i in matrix:
    print(i)