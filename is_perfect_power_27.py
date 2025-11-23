''' question-27: Write a function for Perfect Powers Check is_perfect_power(n)
 that checks if a number can be expressed as a^b where a > 0 and b > 1.'''

import math

def is_perfect_power(n):
    if n <= 1:
        return False

    for b in range(2, int(math.log2(n)) + 2):
        a = round(n ** (1/b))
        if a ** b == n:
            return True

    return False


# Example usage:
print(is_perfect_power(8))   # True (2^3)
print(is_perfect_power(27))  # True (3^3)
print(is_perfect_power(32))  # True (2^5)
print(is_perfect_power(17))  # False
print(is_perfect_power(16))  # True (2^4)
print(is_perfect_power(1))   # False