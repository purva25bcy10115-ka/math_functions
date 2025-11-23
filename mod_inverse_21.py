''' question 21:- Write a function Modular Multiplicative Inverse mod_inverse(a, m)
that finds the number x such that (a*x) = 1 (mod m).'''

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

# Example usage:
print(mod_inverse(3, 11))   # 4
print(mod_inverse(10, 17))  # 12
print(mod_inverse(2, 5))    # 3
print(mod_inverse(5, 12))   # None (Inverse doesn't exist)