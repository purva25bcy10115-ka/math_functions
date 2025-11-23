import time 
starttime=time.time()
def is_palindrome(n):
    if n==n[::-1]:
        print(n)
    else:
        print("the given string is not palindrome")
n= input("enter a string:")
c= is_palindrome(n)
endtime= time.time()
print("the total time required to execute the code in seconds", endtime- starttime, "seconds")