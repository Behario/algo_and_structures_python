# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def multiplicity(range_mass=range(2, 100), range_multiplicity=range(2, 10)):
    list_counter = [0]*8
    for i in range_mass:
        for j in range_multiplicity:
            if i % j == 0:
                list_counter[j-2] += 1
    i = 0
    while i < len(list_counter):
        print(i+2, ' - ', list_counter[i])
        i += 1


multiplicity()