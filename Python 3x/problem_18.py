#this is not accept but i could not find any error
vowel = ['a','e','i','o','u']
num = input()
for n in range(int(num)):
    strVowel = strCons = ''
    inputData = input()
    numList = inputData.replace(" ","")
    for x in numList:
        if x.lower() in vowel:
            strVowel += x
        else:
            strCons += x

    print("{}".format(strVowel))
    print("{}".format(strCons))

#accept this solution
num = int(input())

for x in range(num):
    textInput = input().replace(" ", "")
    vowelLetter = 'aeiou'
    consLetter = 'bcdfghjklmnpqrstvwxyz'
    vowels = ''
    consonent = ''
    for n in textInput:
        if j.lower() in vowelLetter:
            vowels += n
        elif j.lower() in consLetter:
            consonent += n
    print("{}".format(vowels))
    print("{}".format(consonent))
