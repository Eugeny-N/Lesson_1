#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(a,b,c):
    if a > b and a >c:
        if b > c:
            return a + b
        else:
            return a + c
    elif b > a and b > c:
        if a > c:
            return a + b
        else:
            return c + b
    else:
        if a > b:
            return a + c
        else:
            return c + b
print('Сумма наибольших двух аргументов:',my_func(int(input('Введите число №1: ')),int(input('Введите число №2: ')),int(input('Введите число №3: '))))