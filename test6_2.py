def climb(n):
    if n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return climb(n - 1) + climb(n - 2)


n = eval(input())
print(climb(n))
