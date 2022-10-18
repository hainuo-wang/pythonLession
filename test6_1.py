def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)


n = int(input())
count_sum = 0
for i in range(1, n + 1):
    count_sum = count_sum + func(i)
print(count_sum)
