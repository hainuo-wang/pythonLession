username = {'aaa': 123456, 'bbb': 888888, 'ccc': 333333}
username1 = input()
if username1 in username:
    for i in range(0, 3):
        password = input()
        if eval(password) == username[username1]:
            print("Success")
            break
        elif i == 2:
            print("Login Denied")
            break
        print("Fail,{:d}".format(2 - i), "Times Left")
        i = i + 1
else:
    print("Wrong User")
