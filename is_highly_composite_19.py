''' question-19: Write a function is_highly_composite(n) that checks 
 if a number has more divisors than any smaller number.'''

def num_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def is_highly_composite(n):
    n_div = num_divisors(n)
    for i in range(1, n):
        if num_divisors(i) >= n_div:
            return False
    return True

# Example usage:
print(is_highly_composite(1))  # True
print(is_highly_composite(2))  # True
print(is_highly_composite(3))  # False
print(is_highly_composite(4))  # True
print(is_highly_composite(6))  # True
print(is_highly_composite(12)) # True