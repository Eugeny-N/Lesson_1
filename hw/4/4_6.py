#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import count, cycle
for i in count(int(input())):
  print(i, end = ' ')
  quit = input()
  if quit == 'q':
    break
a = input().split()
c = cycle(a)
quit = None
while quit != 'q':
  print(next(c), end = ' ')
  quit = input()