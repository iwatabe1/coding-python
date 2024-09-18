# Fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(5))


# Fibonacci by loop
def loop_finobacci(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = b, a + b
        print(a, b)
    return b


print(loop_finobacci(5))
