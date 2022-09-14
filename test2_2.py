import math

a, b, c = input().split()
a = eval(a)
b = eval(b)
c = eval(c)
if b * b - 4 * a * c < 0:
    print("No")
else:
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
    print("{:.2f} {:.2f}".format(x1, x2))
