# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class DivZer(Exception):
    def __init__(self, txt):
        self.txt = txt
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
try :
    if b == 0:
        raise DivZer('Вы совершаете деление на 0')
    else:
        c = a/b
except DivZer as dz:
    print(dz)
else:
    print(c)