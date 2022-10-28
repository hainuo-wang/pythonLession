a = 100
i = 0
while True:
    i += 1
    try:
        b = eval(input())
    except NameError:
        print('input error')
        continue
    if b > a:
        print("larger than expected")
    elif b < a:
        print("less than expected")
    else:
        print("you have tried {} times, you win".format(i))
        break
