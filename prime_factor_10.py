''' question-10: Write a function prime_factors(n) that returns
 the list of prime factors of a number.'''

def prime_factors(n):
    factors = []
    if n < 2:
        return factors
    
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factors.append(n)

    return factors


# Example usage:
print(prime_factors(12))  # [2, 2, 3]
print(prime_factors(30))  # [2, 3, 5]
print(prime_factors(7))   # [7]