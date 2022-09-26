n = input()
if n.isdigit() or (n[0] == '-' and n.lstrip('-').isdigit()):
    if '3' in n or '4' in n:
        print('true')
    else:
        print('false')
else:
    print('illegal input')
