last = 8888
print(f"Для ряда 0 - {last}\n\n")

from random import randint
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Sum, Avg, Range, Res, RandSum, RandMed, Rand')

(Sum[Range] == sum_(X, for_each = X)) <= X.in_(range_(Range + 1))
print(f"{Sum == Sum[last]}\n\n")

(Avg[Range] == Res) <= (Range / 2 == Res)
print(f"{Avg == Avg[last]}\n\n")

randlist = [randint(0, 99) for _ in range(0, 100)]
randlist.sort()

(Sum[Rand] == sum_(X, for_each = X)) <= X.in_(Rand)
print(f"{Sum[randlist] == RandSum}\n\n")

(RandMed[Rand] == Res) <= ((Rand[49] + Rand[50]) / 2 == Res)
print(RandMed[randlist] == RandMed)