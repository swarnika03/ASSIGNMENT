def func1(main_func,subset_func):
    
    return subset_func in main_func

main_func=input("Enter the main string")
subset_func=input("Enter the substring string")

if func1(main_func,subset_func):
    print("The subset is present in string")

else:
    print("The subset is not  present in string")