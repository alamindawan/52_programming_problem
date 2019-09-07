vouels = ['a','e','i','o','u']
num = input()

for n in range(int(num)):
    inputData = input()
    listData = list(inputData)
    total = 0
    for x in listData:
        if x.lower() in vouels:
            total += 1
    print('Number of vowels = '+str(total))


