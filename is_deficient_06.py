''' question-6: Write a function is_deficient(n) that returns True,
    if the sum of proper divisors of n is less than n.'''

def is_deficient(n):
    if n <= 0:
        return False
    
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum < n

#Example usage:
print(is_deficient(10))  # True → 1+2+5 = 8 < 10
print(is_deficient(12))  # False → 1+2+3+4+6 = 16 > 12