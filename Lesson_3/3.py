#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random
MAX = 9
MIN = 0
LIST_RANDOM = []

for i in range(MIN, MAX + 1):
    RANDOM = int(random() * (MAX - MIN + 1) + MIN)
    LIST_RANDOM.append(RANDOM)

print(LIST_RANDOM)

MINIMUM = min(LIST_RANDOM)
MAXIMUM = max(LIST_RANDOM)
MIN_INDEX = LIST_RANDOM.index(MINIMUM)
MAX_INDEX = LIST_RANDOM.index(MAXIMUM)
LIST_RANDOM[MAX_INDEX], LIST_RANDOM[MIN_INDEX] = LIST_RANDOM[MIN_INDEX], LIST_RANDOM[MAX_INDEX]

print(LIST_RANDOM)