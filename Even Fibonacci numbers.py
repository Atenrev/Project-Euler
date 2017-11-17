act = 1
pre = 0
sumeven = 0

while act < 4000000:
    if act%2==0:
        sumeven+=act
    temp = pre
    pre = act
    act += temp

print (sumeven)
    
