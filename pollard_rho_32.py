''' question-32: Implement pollard_rho() for integer factorization using Pollard's Rho algorithm'''

import random
import math

def pollard_rho(n):
    # Attempts to find a non-trivial factor of n using Pollard's Rho algorithm.
    # Returns a factor d (1 < d < n), or n if no factor is found.

    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n < 2:
        return n

    # Try different constants for function f(x) = x^2 + c
    for c in range(1, 5):
        x = random.randrange(2, n - 1)
        y = x
        d = 1

        while d == 1:
            x = (pow(x, 2, n) + c) % n
            y = (pow(y, 2, n) + c) % n
            y = (pow(y, 2, n) + c) % n
            d = math.gcd(abs(x - y), n)
            if d >= n:
                break

        if 1 < d < n:
            return d

    return n


# Example usage:
print(pollard_rho(91))     
print(pollard_rho(8051))   
print(pollard_rho(17))    
print(pollard_rho(561))