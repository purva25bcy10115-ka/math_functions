''' question-20: Write a function mod_exp(base, exponent, modulus)
 that efficiently calculates (base^exponent) % modulus.'''

def mod_exp(base, exponent, modulus):
    if modulus == 0:
        return None  # can't mod by 0
    
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    
    return result

# Example usage:
print(mod_exp(2, 10, 1000))  # 24
print(mod_exp(3, 13, 7))     # 3
print(mod_exp(7, 128, 13))   # 9
print(mod_exp(12, 21, 17))   # 4