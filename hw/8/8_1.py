#Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, date):
        date = date.split('-')
        self.day = int(date[0])
        self.month = int(date[1])
        self.year = int(date[2])

    @staticmethod
    def check(date):
        date = date.split('-')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        if month < 0 or month > 12:
            print('Неверно введён месяц')
        if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and day > 29:
            print('Неверно введён день')
        elif month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) == False and day > 28:
            print('Неверно введён день')
        else:
            if month < 8 and month % 2 == 1 and day > 31:
                print('Неверно введён день')
            elif month > 7 and month % 2 == 0 and day > 31:
                print('Неверно введён день')
            elif month < 8 and month % 2 == 0 and day > 30:
                print('Неверно введён день')
            elif month > 7 and month % 2 == 1 and day > 30:
                print('Неверно введён день')

    @classmethod
    def translate(cls, date):
        date = date.split('-')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        return [day, month, year]


date1 = Data('12-12-2012')
Data.check('31-12-2012')
print(Data.translate('31-12-2012'))