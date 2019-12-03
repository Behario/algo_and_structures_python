"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

COMPANIES = {}
COMPANY = namedtuple('Company', 'Name income_1 income_2 income_3 income_4')
N = int(input("Введите количество компаний: "))

for i in range(N):
    companie_value = COMPANY(
        Name=(input("Введите название: ")),
        income_1=float(input("Введите прибыль за 1 квартал: ")),
        income_2=float(input("Введите прибыль за 2 квартал: ")),
        income_3=float(input("Введите прибыль за 3 квартал: ")),
        income_4=float(input("Введите прибыль за 4 квартал: ")),
    )
    COMPANIES_INCOME_AVERAGE = float((companie_value.income_1 + companie_value.income_2
                                             + companie_value.income_3
                                             + companie_value.income_4) / 4)
    COMPANIES[companie_value.Name] = COMPANIES_INCOME_AVERAGE

SUM_AVG_COMPANY = 0
for i in COMPANIES:
    SUM_AVG_COMPANY += COMPANIES[i]

AVG = SUM_AVG_COMPANY / N

print(f"Средняя прибыль у компаний по рынку: {round(AVG, 3)}")

for i in COMPANIES:
    if COMPANIES[i] > AVG:
        print(f"{i}: средняя прибыль {round(COMPANIES[i], 3)} - прибыль выше средней по рынку")
    elif COMPANIES[i] == AVG:
        print(f"{i}: средняя прибыль {round(COMPANIES[i], 3)} - прибыль равна средней по рынку")
    elif COMPANIES[i] < AVG:
        print(f"{i}: средняя прибыль {round(COMPANIES[i], 3)} - прибыль ниже средней по рынку")
