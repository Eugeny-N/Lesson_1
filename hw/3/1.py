#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def func(a,b):
    while b == 0:
        print('Деление на ноль!!!')
        b = int(input('Введите делитель '))
    return (a/b)


a = int(input('Введите делимое '))
b = int(input('Введите делитель '))
print(func(a,b))