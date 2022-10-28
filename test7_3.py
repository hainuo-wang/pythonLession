def count(t):
    u = l = d = s = others = 0
    for i in t:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
        elif i.isnumeric():
            d += 1
        elif i.isspace():
            s += 1
        else:
            others += 1
    print(u, l, d, s, others)


def word(fr):
    sum = 0
    for line in fr:
        for j in '.' + ',' + "'":
            line = line.replace(j, '')
        ls = line.split(" ")
        sum += len(ls)
    return sum


def shiftkey(x):
    sum = 0
    for j in x:
        sum += ord(j)
    return sum


def shift(t, r):
    s = ''
    for i in t:
        if i.isupper():
            i = chr(ord('A') + (ord(i) - ord('A') + r) % 26)
        elif i.islower():
            i = chr(ord('a') + (ord(i) - ord('a') + r) % 26)
        s += i
    return s


key = shiftkey(input()) % 26
fr = open("mayun.txt", "r")
t = fr.read()
fr.seek(0)

count(t)
print("{} words in all".format(word(fr)))
print(key)
print(shift(t, key))

fr.close()
