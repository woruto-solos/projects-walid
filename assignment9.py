j=input("lide it in")
k=int(j)
int_num=k+1
while (int_num>0):
    int_num=int_num-1
    if int_num%3==0 and int_num%5==0:
        print(int_num,"fizzbuzz")    
    elif int_num%3==0:
        print(int_num,"fizz")  
    elif int_num%5==0:
        print(int_num,"chuzz")
    elif int_num%15==0:
        print(int_num,"huzz")
    else :
        print(int_num,"no divisable by 5 or 3")

    