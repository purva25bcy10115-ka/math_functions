''' question-8: Write a function is_automorphic(n) that checks
 if a number's square ends with the number itself.'''

def is_automorphic(n):
    square = n ** 2
    return str(square).endswith(str(n))

# Example usage
print(is_automorphic(5))   # True → 5^2 = 25 ends with 5
print(is_automorphic(6))   # True → 36 ends with 6
print(is_automorphic(7))   # False → 49 doesn't end with 7
print(is_automorphic(76))  # True → 5776 ends with 76