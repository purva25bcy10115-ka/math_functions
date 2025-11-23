'''question-5: Write a function is_abundant(n) that returns True if the ,sum of proper divisors of n is greater than n.'''

import time

starttime = time.time()

def is_abundant(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum > n

n = int(input("Enter a number: "))
c = is_abundant(n)
print(c)

endtime = time.time()
print("Total time required to execute the code in seconds:", endtime - starttime, "seconds")