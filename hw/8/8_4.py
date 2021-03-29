# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage():
    def __init__(self):
        self
class Org():
    def __init__(self,mass):
        self.mass = mass
class Printer(Org):
    def __init__(self, paper):
        self.paper = paper
class Scaner(Org):
    def __init__(self,resol):
        self.resol = resol
class Xerox(Org):
    def __init__(self,copi):
        self.copi = copi