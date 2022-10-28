goal = 100
while True:
    guess = int(input())
    if guess < goal:
        print("less than expected")
    elif guess > goal:
        print("larger than expected")
    else:
        print("you win")
        break
