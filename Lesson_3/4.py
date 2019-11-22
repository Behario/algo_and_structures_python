# 4.	Определить, какое число в массиве встречается чаще всего.
from random import random
MAX = 100
MIN = 0
RANGE = 20
LIST_RANDOM = []

for i in range(RANGE):
    RANDOM = int(random() * (MAX - MIN + 1) + MIN)
    LIST_RANDOM.append(RANDOM)

print(LIST_RANDOM)

NUMBER_LIST = []
MAX_COUNTER = 1

for i in range(RANGE-1):
    counter = 1
    for j in range(i+1, RANGE):
        if LIST_RANDOM[i] == LIST_RANDOM[j]:
            counter += 1
    if counter > MAX_COUNTER:
        MAX_COUNTER = counter
        NUMBER_LIST = LIST_RANDOM[i]

if MAX_COUNTER > 1:
    print(f"{MAX_COUNTER} раз(а) встречается число {NUMBER_LIST}")
else:
    print('Повторяющихся элементов нет')