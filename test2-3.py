s = input()
str_upper, str_lower, num = 0, 0, 0
for i in s:
    if i.islower():
        str_lower += 1
    elif i.isupper():
        str_upper += 1
    elif i.isdigit():
        num += 1
print(str_upper)
print(str_lower)
print(num)
