''' question-14: Write a function twin_primes(limit) that generates 
 all twin prime pairs up to a given limit.'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def twin_primes(limit):
    twins = []
    for num in range(2, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            twins.append((num, num + 2))
    return twins

# Example usage:
print(twin_primes(30))  # [(3, 5), (5, 7), (11, 13), (17, 19)]