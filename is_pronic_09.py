''' question-9: Write a function is_pronic(n) that checks
 if a number is the product of two consecutive integers.'''

def is_pronic(n):
    if n < 0:
        return False
    
    i = 0
    while i * (i + 1) <= n:
        if i * (i + 1) == n:
            return True
        i += 1
        
    return False

# Example usage
print(is_pronic(6))   # True → 2 * 3
print(is_pronic(12))  # True → 3 * 4
print(is_pronic(20))  # True → 4 * 5
print(is_pronic(10))  # False