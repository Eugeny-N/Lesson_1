#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
def my_func(x, y):
    s = x
    y = -y
    for i in range(y-1):
        s *=x
    s = 1/s
    #s = x**y
    return s
print(my_func(3,-3))

range(6)