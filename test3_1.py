sum = 0
n = 0
x = 0
y = 0
number = 1
while number != 0:
    number = eval(input(""))
    sum = sum + number
    n = n + 1
    if number<0:
        x = x + 1
    else:
        y = y + 1
average = sum/(n-1);
print(average)
print(y-1)
print(x)