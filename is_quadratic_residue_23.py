''' question 23: Write a function Quadratic Residue
Check is_quadratic_residue(a, p) that checks if x^2 = a mod p has a solution.'''

def is_quadratic_residue(a, p):
    # Using Euler's Criterion: a^((p-1)/2) ≡ 1 (mod p)
    return pow(a, (p - 1) // 2, p) == 1

# Example usage:
print(is_quadratic_residue(2, 7))   # True
print(is_quadratic_residue(3, 7))   # False
print(is_quadratic_residue(5, 11))  # True
print(is_quadratic_residue(4, 13))  # True