from math import sqrt
from time import time

primes = [2]


def new_square(old_n):
    n = old_n + 1
    square = n ** 2
    return square, n


def inner_loop(num, base_in):
    for x in primes:
        if num % x == 0:
            return False
        if x >= base_in:
            return True


start = time()

square, base = new_square(1)


for i in range(3, 25000000, 2):
    if i > square:
        square, base = new_square(base)
    is_prime = inner_loop(i, base)
    if is_prime:
        primes.append(i)


end = time()
print(primes[-1])
print(end - start)
