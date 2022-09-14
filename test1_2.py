tem = input("What is the temperature?")
if tem[-1] == "F":
    result = (eval(tem[0:-1]) - 32) / 1.8
    symbol = "C"
    print("The converted temperature is {}{}".format(int(result), symbol))
elif tem[-1] == "C":
    result = eval(tem[0:-1]) * 1.8 + 32
    symbol = "F"
    print("The converted temperature is {}{}".format(int(result), symbol))
else:
    print("input error!")
