''' question-12: Write a function is_prime_power(n) that checks 
if a number can be expressed as p^k where p is prime and k >= 1'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_power(n):
    if n < 2:
        return False
    
    # Try every prime number p up to sqrt(n)
    for p in range(2, int(n**0.5) + 2):
        if is_prime(p):
            temp = p
            while temp <= n:
                if temp == n:
                    return True
                temp *= p
    return False

# Example usage
print(is_prime_power(1))   # False
print(is_prime_power(2))   # True → 2^1
print(is_prime_power(4))   # True → 2^2
print(is_prime_power(8))   # True → 2^3
print(is_prime_power(9))   # True → 3^2
print(is_prime_power(12))  # False
print(is_prime_power(27))  # True → 3^3
print(is_prime_power(30))  # False
print(is_prime_power(49))  # True → 7^2
print(is_prime_power(64))  # True → 2^6
print(is_prime_power(100)) # False