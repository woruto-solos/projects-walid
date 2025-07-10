word=input("give me a word: ")
num=int(input("give me a number: "))

if len(word)>num:
 num=num-1
 print (word[num])
else:
 print("invalid")