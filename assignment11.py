word=input("give me a word: ")
counter=0
for letter in word:
    if letter=="a" or letter=="e" or letter=="i" or letter=="u" or letter=="o":
      counter=counter+1
print(counter)
