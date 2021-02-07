#input a sentence from the user and count the no of words in it

userword = input("Enter your sentence here: ")
print(userword)

charactercount = 0
wordcount = 1
for i in userword:
    charactercount = charactercount + 1
    if(i==' '):
        wordcount = wordcount + 1


print(charactercount)
print(wordcount)
