## wrong: permutable primes instead of circular primes
import itertools as it
import time
def p35():
    
    n = int(input("Number of permutable primes under: "))
    time0 = time.time()
    
    ## generates list of primes
    primeList = [2]
    for x in range(3, 10**(len(str(n))), 2):
        isPrime = True
        for y in range(2, int(x**0.5)+1):
            if x % y == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(x)

    
    ## generates list of permutations of every prime
    permList = []
    for i in primeList:
        digits = [int(x) for x in str(i)]
        nPower = len(digits)-1
        permutations = it.permutations(digits)
        permList.append([sum(v*(10**(nPower-i)) for i, v in enumerate(item)) for item in permutations])

    ## checks if all elements in permList are in primeList
    circList = []
    for a in permList:
        if set(a).issubset(primeList):
            circList.append(a[0])

    ## removes extra primes
    finList = []
    for b in circList:
        if b <= n:
            finList.append(b)
    print("There are %s circular primes under " %(len(finList)) + "%s:" %(n))
    print(finList)
    print("Runtime: %.4fs seconds" %(time.time() - time0))
p35()
