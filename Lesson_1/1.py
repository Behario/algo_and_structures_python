# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
m = int(input("Введите трехзначное число: "))
a = m % 10
b = m % 100 // 10
c = m % 1000 // 100
sum = a + b + c
mult = a * b * c

print(f"Сумма составных чисел = {sum}, произведение = {mult}")