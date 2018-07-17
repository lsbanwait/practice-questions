##reasonable up to 8 decimals (4 secs)
import math
import time
from fractions import Fraction

exp = input("Accurate to how many decimal places: ")
startTime = time.time()
##def piApprox():
for i in range(1, 1000000001):
    if abs((int(round(math.pi*i))) - (math.pi*i)) < 10**(-(int(exp)-1)):        
        print("The smallest approximation is %s." %(Fraction(int(round(math.pi*i)), i)))
        break
print("%.3fs seconds" %(time.time()-startTime))


        
