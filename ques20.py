
numbers = input("Enter a list of numbers with  spaces: ").split()

numbers = [int(num) for num in numbers]
total_sum = sum(numbers)
print("The sum of the numbers is: ",total_sum)