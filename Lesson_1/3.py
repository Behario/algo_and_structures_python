# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.


def makeFixed(num_float, digits):
    return f"{num_float:.{digits}f}"


X1 = float(input("Введите значение координаты x1: "))
Y1 = float(input("Введите значение координаты y1: "))
X2 = float(input("Введите значение координаты x2: "))
Y2 = float(input("Введите значение координаты y4: "))

K = -1 * (Y2 - Y1)/(X1 - X2)
B = -1 * (X2*Y1 - X1*Y2)/(X1 - X2)

print(f"Уравнение имеет вид y = {makeFixed(K, 3)}x + {makeFixed(B, 3)}")
