''' question-28: Write a function Collatz Sequence Length collatz_length(n)
that returns the number of steps for n to reach 1 in the Collatz conjecture.'''

def collatz_length(n):
    if n < 1:
        return 0
    
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count


# Example usage:
print(collatz_length(6))
print(collatz_length(7))
print(collatz_length(1))
print(collatz_length(13))