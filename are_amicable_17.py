''' question-17: Write a function are_amicable(a, b) that checks 
 if two numbers are amicable (sum of proper divisors match each other)'''

def aliquot_sum(n):
    return sum(i for i in range(1, n) if n % i == 0)

def are_amicable(a, b):
    return aliquot_sum(a) == b and aliquot_sum(b) == a

# Example usage:
print(are_amicable(220, 284))     # True
print(are_amicable(1184, 1210))   # True
print(are_amicable(6, 28))        # False
print(are_amicable(2620, 2924))   # True