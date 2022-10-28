n = int(input())
s = [0] * n
ans = []
num = 1
x, y, i, j = 0, 0, 0, 0
for i in range(n):
    ans.append(s[:])
i = 0
q = n*n
while num <=q :
    for p in range(n):
        ans[i][j] = num
        num += 1
        j+=1
    n -= 1
    i += 1
    j -= 1
    for p in range(n):
        ans[i][j] = num
        num += 1
        i += 1
    i -= 1
    j -= 1
    for p in range(n):
        ans[i][j] = num
        num += 1
        j -=1
    j += 1
    i -= 1
    n -=1
    for p in range (n):
        ans[i][j] = num
        num += 1
        i -= 1
    i += 1
    j += 1
with open("file.out", "w") as file:
    for p in ans:
        for f in p:
            file.write("%5d"%f)
        file.write("\n")
