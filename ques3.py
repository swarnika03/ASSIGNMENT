def func1(num):
    if num==1 or num==0:
        return 1
    elif num<0:
        print("cant print")
    else:
        return (num*func1(num-1))    




num=int(input("Enter any number"))
res=func1(num)
print("the answer is {num}",res)
