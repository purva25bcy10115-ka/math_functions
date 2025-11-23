import time
starttime=time.time()
def mean_of_digits(n):
    s= str(abs(n))
    total = 0
    for digit in s:
        total += int (digit)
    return total / len (s)
n=int (input ("enter a number:"))
c = mean_of_digits(n)
print (c)
endtime = time.time()
print ("total time required to execute the code in seconds", endtime - starttime, "seconds")