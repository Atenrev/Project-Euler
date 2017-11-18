x = 2520
found = False

while not found:
    x+=20
    found = True
    for i in range(11,21):
        if x%i!=0:
            found = False
            
print (x)
