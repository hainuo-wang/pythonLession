n, str = input().split(' ', 1)
list = []
for p in str:
    if "A" <= p <= "Z":
        print(chr(ord("A") + (ord(p) - ord("A") + int(n)) % 26), end="")
    elif "a" <= p <= "z":
        print(chr(ord("a") + (ord(p) - ord("a") + int(n)) % 26), end="")
    else:
        print(p, end="")

