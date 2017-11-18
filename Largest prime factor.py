import math

inNum = 600851475143

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

for x in reversed(range(2, int(math.sqrt(inNum)))):
    if inNum%x==0 and prime(x):
        print (x)
        break
    

    
