# map filter reduce

def factorial(n):
    """return n!"""
    return 1 if n < 2 else n*factorial(n-1)

print("5! = %d", factorial(5))
print("5! = %d" % factorial(5))
print("5! = {}".format(factorial(5)))
print("5! = {0}".format(factorial(5)))

# high-order function

print("--- --- --- --- ")

fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banna"]
sorted_fruit = sorted(fruits, key=len)

print("sorted_fruit is : {}".format(sorted_fruit))


def reverse(word):
    return word[::-1]

print("reverse('testing' = {}".format(reverse('testing')))

print("sorted(fruits, key=reverse)  =- {}".format(sorted(fruits, key=reverse)))

print("--- --- --- --- ")

print(range(6))
print(list(map(factorial, range(6))))

print(list(map(factorial, filter(lambda n: n%2, range(6)))))
print([factorial(n) for n in range(6) if n%2])

from functools import reduce
from operator import add
print(reduce(add,range(100)))
print(sum(range(100)))

print("--- --- --- --- ")

import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("Pick from empty BingoCage")

    def __call__(self):
        return self.pick()

    def __repr__(self):
        return 'BingoCage list = {}'.format(self._items)      # %r 代表对象

bingo = BingoCage(range(3))
print(bingo) # __repr__
print(bingo.pick())
print(bingo)    # __call__
print(bingo())
print(callable(bingo))
print(bingo)

print("--- --- --- --- ")