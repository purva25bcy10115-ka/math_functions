''' question-29: Write a function Polygonal Numbers polygonal_number(s, n)
that returns the n-th s-gonal number.'''

def polygonal_number(s, n):
    if s < 3 or n < 1:
        raise ValueError("s must be ≥ 3 and n must be ≥ 1")

    # Formula: P(s, n) = ((s - 2) * n * (n - 1)) // 2 + n
    return ((s - 2) * n * (n - 1)) // 2 + n


# Example usage:
print(polygonal_number(3, 5))  # 5th triangular number
print(polygonal_number(4, 4))  # 4th square number
print(polygonal_number(5, 2))  # 2nd pentagonal number
print(polygonal_number(6, 3))  # 3rd hexagonal number