

'''que-31:-Implement the probabilistic Miller-Rabin test is_prime_miller_rabin(n, k) with k rounds...'''

import random

def is_prime_miller_rabin(n, k):
    # Miller-Rabin probabilistic primality test.
    # Returns True if n is probably prime, False if composite.
    # k is the number of testing rounds.

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d with d odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # composite

    return True  # probably prime


# Example usage:
print(is_prime_miller_rabin(17, 5))
print(is_prime_miller_rabin(561, 5))
print(is_prime_miller_rabin(101, 2))
print(is_prime_miller_rabin(1000003, 5))
print(is_prime_miller_rabin(1000004, 5))