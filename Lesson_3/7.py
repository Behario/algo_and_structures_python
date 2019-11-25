"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
LIST = [1, 1, -56, -5, 45, -46, -6, 1, 3]
N = len(LIST)
INDEX_MIN_1 = 0
INDEX_MIN_2 = 0

for i in range(N):
    if LIST[i] < LIST[INDEX_MIN_1]:
        INDEX_MIN_1 = i

LIST_DUPLE = LIST[:]
LIST_DUPLE = LIST_DUPLE[:INDEX_MIN_1] + LIST_DUPLE[INDEX_MIN_1+1:]
A = len(LIST_DUPLE)

for j in range(A):
    if LIST_DUPLE[j] < LIST_DUPLE[INDEX_MIN_2]:
        INDEX_MIN_2 = j

print(f"Минимальный элемент 1 = {LIST[INDEX_MIN_1]}\n"
      f"Минимальный элемент 2 = {LIST_DUPLE[INDEX_MIN_2]}")