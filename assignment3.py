while True:
    num=input("give me a number: ")
    num2=input("give me a 2nd number")

    wd=input("whactha wanan do:")
    int_num=int(num)
    int_num2=int(num2)
    if wd=="add":
        result=int_num+int_num2
        print (result)
    elif wd=="subtract":
        result=int_num-int_num2
        print (result)
    elif wd=="multiply":
        result=int_num*int_num2
        print (result)
    elif wd=="divide":
        result=int_num/int_num2
        print (result)
    elif wd=="power":
         result=int_num**int_num2
         print(result)
    else:
        print("you suck")
        break






