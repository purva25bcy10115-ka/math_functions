''' question-16: Write a function aliquot_sum(n) that returns 
 the sum of all proper divisors of n (divisors less than n).'''

def aliquot_sum(n):
    return sum(i for i in range(1, n) if n % i == 0)

# Example usage:
print(aliquot_sum(6))   # 1+2+3 = 6
print(aliquot_sum(12))  # 1+2+3+4+6 = 16
print(aliquot_sum(15))  # 1+3+5 = 9
print(aliquot_sum(28))  # 1+2+4+7+14 = 28