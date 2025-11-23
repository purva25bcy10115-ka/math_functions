''' question-18: Write a function multiplicative_persistence(n)
that counts how many steps until a number's digits multiply to a single digit.'''

def multiplicative_persistence(n):
    steps = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)  # <-- THIS was missing
        n = product
        steps += 1
    return steps

# Example usage:
print(multiplicative_persistence(39))   # 3 steps → 39 → 27 → 14 → 4
print(multiplicative_persistence(77))   # 4 steps → 77 → 49 → 36 → 18 → 8
print(multiplicative_persistence(4))    # 0 steps (already single digit)
print(multiplicative_persistence(999))  # 4 steps