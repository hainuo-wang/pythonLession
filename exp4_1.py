for i in range(0, 100):
    s = str(i ** 3) + str(i ** 4)
    if len(str(i ** 3)) == 4 and len(str(i ** 4)) == 6 and len(set(s)) == 10:  # 判断元素个数是否相同
        print(i)
        break
