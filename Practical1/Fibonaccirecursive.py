def recursive_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


# Example usage:
n = 29  # Change this to calculate Fibonacci for a different value of n
result = recursive_fibonacci(n)
print(f"The {n}-th Fibonacci number is {result}")
