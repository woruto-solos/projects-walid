num=input("give me a number")
x=int(num)
if x%3==0 and x%5==0:
    print("fizzbuzz")
elif x%3==0:
    print("fizz")
elif x%5==0:
    print("huzz")
elif x%15==0:
    print("huzz")
else :
    print("no divisable by 5 or 3")