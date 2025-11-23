''' question-15: Write a function count_divisors(n) that returns 
how many positive divisors a number has.'''

def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# Example Usage:
print(count_divisors(1))   # 1
print(count_divisors(6))   # 4 → 1,2,3,6
print(count_divisors(10))  # 4 → 1,2,5,10
print(count_divisors(12))  # 6 → 1,2,3,4,6,12
print(count_divisors(17))  # 2 → 1,17 (prime)
print(count_divisors(36))  # 9
print(count_divisors(100)) # 9