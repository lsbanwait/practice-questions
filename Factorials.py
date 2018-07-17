import time
n = int(input("Factorial of: "))
start_time = time.time()

def factorial(n):
    if n<=1:
        return(1)
    else:
        return (n*factorial(n-1))

print (factorial(n))
print("%.3fs seconds" %(time.time() - start_time))
