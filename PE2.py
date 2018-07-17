## fibo(x) instead of input
def fibo():
    a=0
    b=1
    list=[0]
    while b-a<800:
        a=b-a
        b=a+b
        if a%2==0:
            list.append(a)
    print (sum(list))
    
        
        
        
    
