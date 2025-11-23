''' question-11: Write a function count_distinct_prime_factors(n)
that returns how many unique prime factors a number has.'''

def count_distinct_prime_factors(n):
    if n <= 1:
        return 0

    factors = set()
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factors.add(n)

    return len(factors)

# Example usage:
print(count_distinct_prime_factors(12))  # 2 (2, 3)
print(count_distinct_prime_factors(30))  # 3 (2, 3, 5)
print(count_distinct_prime_factors(7))   # 1 (7)
print(count_distinct_prime_factors(60))  # 3 (2, 3, 5)
print(count_distinct_prime_factors(100)) # 2 (2, 5)
print(count_distinct_prime_factors(1))   # 0