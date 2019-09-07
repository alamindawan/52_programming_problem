c = input()
for x in range(int(c)):
    d = input()
    for y in range(int(d)):
        for z in range(int(d)):
            print("*",end = '')
        print()
    if x < int(c)-1:
        print()
