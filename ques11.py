def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    return fib_sequence

#
n = int(input("Enter the fibonacci number till to generate sequence"))
fib_sequence = fibonacci(n)
print(f"The first ",n," numbers in the Fibonacci sequence are:",fib_sequence)