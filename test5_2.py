def fac(x):
    for a in range(2, x):
        b = 0
        for i in range(1, a):
            if a % i == 0:
                b += i

        r = 0
        for j in range(1, b):
            if b % j == 0:
                r += j

        if r == a and a < b:
            print("{} {}".format(a, b))


n = int(input())
fac(n)

