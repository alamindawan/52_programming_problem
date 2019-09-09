

#accept this solution
num = int(input())

for x in range(num):
    anotherInput = input().replace(" ", "")
    vowelLetter = 'aeiou'
    consLetter = 'bcdfghjklmnpqrstvwxyz'
    vowels = ''
    consonent = ''
    for n in anotherInput:
        if n.lower() in vowelLetter:
            vowels += n
        elif n.lower() in consLetter:
            consonent += n
    print("{}".format(vowels))
    print("{}".format(consonent))
