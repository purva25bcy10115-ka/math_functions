''' question-30: Carmichael Number Check'''

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_carmichael(n):
    # Must be composite
    if n < 3 or is_prime(n):
        return False

    # Check Fermat-like condition for all a coprime to n
    for a in range(2, n):
        if gcd(a, n) == 1:
            if pow(a, n-1, n) != 1:
                return False

    return True


# Example usage:
print(is_carmichael(561))   # True
print(is_carmichael(1105))  # True
print(is_carmichael(15))    # False
print(is_carmichael(7))     # False (it's prime)
print(is_carmichael(9))     # False