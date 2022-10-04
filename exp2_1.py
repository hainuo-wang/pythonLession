head, foot = map(int, input().split(' '))
for hen in range(1, head):
    rabbit = head - hen
    if 2 * hen + 4 * rabbit == foot:
        print(hen, rabbit)
        exit()
print("Data Error!")
