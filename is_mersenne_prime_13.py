''' question-13: Write a function is_mersenne_prime(p) that checks 
if 2^p - 1 is prime (p itself must be prime)'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    
    m = (2 ** p) - 1
    return is_prime(m)

# Example usage
print(is_mersenne_prime(2))   # True → 3
print(is_mersenne_prime(3))   # True → 7
print(is_mersenne_prime(5))   # True → 31
print(is_mersenne_prime(7))   # True → 127
print(is_mersenne_prime(11))  # False
print(is_mersenne_prime(13))  # True → 8191
print(is_mersenne_prime(17))  # True → 131071
print(is_mersenne_prime(19))  # True → 524287
print(is_mersenne_prime(23))  # False