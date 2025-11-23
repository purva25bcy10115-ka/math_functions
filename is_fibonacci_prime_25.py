''' question 25: Write a function Fibonacci Prime Check is_fibonacci_prime(n)
 that checks if a number is both Fibonacci and prime.'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_fibonacci(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    return int(x1*0.5)*2 == x1 or int (x2**0.5)*2 == x2


def is_fibonacci_prime(n):
    return is_fibonacci(n) and is_prime(n)


# Example usage:
print(is_fibonacci_prime(2))
print(is_fibonacci_prime(5))
print(is_fibonacci_prime(13))
print(is_fibonacci_prime(21))
print(is_fibonacci_prime(7))