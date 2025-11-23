''' question 22: Write a function Chinese Remainder Theorem
 Solver crt(remainders, moduli) that solves a system of congruences x = rᵢ (mod mᵢ)'''

def mod_inverse(a, m):
    m0 = m
    x0, x1 = 0, 1

    if m == 1:
        return None

    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += m0

    return x1

def crt(remainders, moduli):
    from functools import reduce
    
    assert len(remainders) == len(moduli)

    M = reduce(lambda x, y: x * y, moduli)
    solution = 0

    for r, m in zip(remainders, moduli):
        Mi = M // m
        inv = mod_inverse(Mi, m)
        solution += r * Mi * inv

    return solution % M

# Example usage:
print(crt([2, 3, 2], [3, 5, 7]))       # Output: 23
print(crt([1, 2, 3], [2, 3, 5]))       # Output: 23
print(crt([4, 6], [5, 7]))             # Output: 34