from math import sqrt
from time import time

primes = [2]


def inner_loop(num):
    root = sqrt(num)
    for x in primes:
        if num % x == 0:
            return False
        if x >= root:
            return True


start = time()


for i in range(3, 25000000, 2):
        is_prime = inner_loop(i)
        if is_prime:
            primes.append(i)

print(primes[-1])


end = time()
print(end - start)
