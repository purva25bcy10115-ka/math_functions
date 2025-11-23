import time
starttime=time.time ()
def factorial (n) :
    if n< 0:
        raise ValueError ("Input must be a non-negative integer.")
    result = 1
    for i in range (2, n + 1):
        result *= i
    return result
n = int (input("enter a number:"))
c= factorial (n)
print ("the factorial of ",n, "is", c)
endtime = time.time ()
print ("total time required to execute the code in seconds", endtime - starttime,"seconds")