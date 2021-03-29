# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Komplex():
    def __init__(self, ch):
        self.ch = ch

    def __add__(self, other):
        return self.ch + other.ch

    def __radd__(self, other):
        return self.ch + other.ch

    def __mul__(self, other):
        return self.ch * other.ch


a = Komplex(complex(1 + 2j))
b = Komplex(complex(2 + 3j))
print(a + b)
print(a * b)