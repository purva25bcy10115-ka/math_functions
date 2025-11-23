''' question-7: Write a function is_harshad(n) that checks
if a number is divisible by the sum of its digits.'''

def is_harshad(n):
    if n == 0:
        return False
    
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0

# Example usage
print(is_harshad(18))  # True → 1+8 = 9 → 18 % 9 = 0
print(is_harshad(21))  # True → 2+1 = 3 → 21 % 3 = 0
print(is_harshad(19))  # False → 1+9 = 10 → 19 % 10 != 0