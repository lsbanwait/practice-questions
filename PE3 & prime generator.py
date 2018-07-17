import math
import time
n = int(input("Prime ceiling: "))
start_time = time.time()
count = 0
if n > 1:
    count = 1
isPrime = False
##total = 2 for sum
for x in range(3, n + 1, 2):
    isPrime = True
    for y in range(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            isPrime = False
            break
    if isPrime:  ##and str(x) == str(x)[::-1] for palindrome
        count += 1  ##total += x for sum
##print(primeList)  ##(total) for sum
print("There are %s primes under " %count + "%s" %n + ".")
print("%.3fs seconds." %(time.time() - start_time))
print("The ratio of primes to natural numbers is %s." %(count/n))

##to print a list of primes
##def primeGen():
##    import math
##    import time
##    ##n = int(input("Prime ceiling: "))
##    n = 10000000
##    start_time = time.time()
##    primeList = []
##    ##total = 2 for sum
##    if n > 1:
##        primeList.append(2)
##    for x in range(3, n + 1, 2):
##        isPrime = True
##        for y in range(2, int(math.sqrt(x)) + 1):
##            if x % y == 0:
##                isPrime = False
##                break
##        if isPrime:  ##and str(x) == str(x)[::-1] for palindrome
##            primeList.append(x)  ##total += x for sum
##    print(primeList)  ##(total) for sum
##    print("%s seconds" %(time.time() - start_time))

##def pEuler3():
##    pENum = int(input("Prime factor of which number?: "))
##    primeProduct = []
##    for i in primeGen.primeList:
##        if pENum % i == 1:
##            primeProduct.append(i)
##    return (primeProduct[-1])
##
##print("The largest prime factor is " %  + str(pEuler3()))
