"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

LIST = [23, -5, 6, 8, 1, 1.31, -15, 1, 2, 3, 55, 44]
INDEX_MAX = 0
INDEX_MIN = 0

for i in range(len(LIST)):
    if LIST[i] > LIST[INDEX_MAX]:
        INDEX_MAX = i
    elif LIST[i] < LIST[INDEX_MIN]:
        INDEX_MIN = i

if INDEX_MAX < INDEX_MIN:
    INDEX_MAX, INDEX_MIN = INDEX_MIN, INDEX_MAX

SUM = 0

for j in range(INDEX_MIN+1, INDEX_MAX):
    SUM += LIST[j]

print(SUM)
