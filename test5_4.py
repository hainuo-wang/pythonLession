def isprime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


def f(n):
    b = []
    for c in range(n+1, 1, -1):
        if len(b) < 10 and isprime(c):
            b.append(c)
    return b


n = int(input())
b = f(n)
print(sum(b))
