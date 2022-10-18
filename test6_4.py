import math


def prime(p):
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


n = int(input())
if n % 2 == 0:
    for i in range(2, int(n / 2) + 1):
        if prime(i) and prime(n - i):
            print("N", "=", i, "+", n - i)
            break
else:
    print("Data error!")
