''' question-26: Write a function Lucas Numbers Generator lucas_sequence(n)
that generates the first n Lucas numbers (starts with 2, 1).'''

def lucas_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]

    lucas = [2, 1]
    for i in range(2, n):
        lucas.append(lucas[-1] + lucas[-2])
    return lucas


# Example usage:
print(lucas_sequence(5))
print(lucas_sequence(10))