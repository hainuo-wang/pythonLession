a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
print("".join([str(q) for q in sorted((list(set(a+b))))]))