def cmul(a, *b):
    for i in b:
        a *= i
    return a


print(eval("cmul({})".format(input())))