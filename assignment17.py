import random
def lucky_guess(guess,range_number):
    random_guess=random.randint(1, range_number)
    for attempt in range(1,6):
        if guess==random_guess:
            print("success")
            break
        else:
            print("try agian")
        guess=int(input("Take ANother gguess"))
lucky_guess(4,50)