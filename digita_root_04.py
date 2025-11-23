import time
starttime=time.time()
def digital_root(n):
    while n>=10:
        n= sum(int(d) for d in str(n))
    return n
n= int(input("enter a number:"))
c= digital_root(n)
print(c)
endtime= time.time()
print("total time required to execute the code in seconds", endtime-starttime,"seconds")
