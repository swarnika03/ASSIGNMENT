def func1(num):
    sum=0
    while(num):
       a=num%10
       sum=sum+a
       num=int(num/10)
    
    return sum

num=int(input("Enter the number"))
res=func1(num)
print("The sum of digit  is",res)