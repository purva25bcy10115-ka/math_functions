'''question 24:- Write a function order_mod(a, n) that finds the smallest positive integer k such that a^k ≡ 1 (mod n).'''

def order_mod(a, n):
    if n <= 1 or a <= 0:
        return None
    
    k = 1
    while k <= n:   # brute force search for smallest k
        if pow(a, k, n) == 1:
            return k
        k += 1
    
    return None  # No multiplicative order found

# Example usage:
print(order_mod(2, 7))   # 3
print(order_mod(3, 7))   # 6
print(order_mod(10, 17)) # 16
print(order_mod(2, 9))   # None (2 is not coprime with 9)