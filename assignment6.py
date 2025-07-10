import random
playing=True
while(playing):
    secret_number=random.randint(1,25)
    guess_number=int(input("Guess a number"))
    if (secret_number==guess_number):
        print("You win")
    else:
        print("you are wrong")
    play_again=input("do you want to continue?")
    if (play_again=="yes"):
      playing=True
    else:
        playing=False

#number=random.randint(1,5)
#print("Enter a random number between 1 and 5: ")
#while True:
   # x=input()
   # winner=int(x)
   # if winner<number:
     #   print("bigger")
   # if winner>number:
      #  print("smaller")
  #  elif winner==number :
     #   print("you win" )
   # break 

#number=random.randint(1,5)

