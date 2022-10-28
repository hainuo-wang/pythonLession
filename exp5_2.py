n = int(input())
a = [[1], [1, 1]]
for j in range(n - 2):
    new = [1]
    b = a[-1]
    for i in range(len(b) - 1):
        new.append(b[i] + b[i + 1])
    new.append(1)
    a.append(new)
l = len(str(max(a[n - 1])))
for i in a:
    print(" " * (l * (n - len(i))), end = "")
    for j in i:
        print(" " * (l - len(str(j))), end = "")
        print(j, end = "")
        print(" " * l, end = "")
    print(end = "\n")
