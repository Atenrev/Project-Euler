inNum = 600851475143

def prime(n):
    for x in range(2,n):
        if n%x==0:
            return False
    return True

for x in reversed(range(2, inNum)):
    if inNum%x==0 and prime(x):
        print (x)
        break
