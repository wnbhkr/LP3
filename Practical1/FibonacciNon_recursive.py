def iterative_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


# Example usage:
n = 37  # Change this to calculate Fibonacci for a different value of n
result = iterative_fibonacci(n)
print(f"The {n}-th Fibonacci number is {result}")
