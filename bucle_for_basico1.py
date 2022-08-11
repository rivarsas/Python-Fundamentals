# Punto 1

for x in range(0,151):
    print(x)

# Punto 2

for x in range(1,1001):
    if (x%5==0):
        print (x)

for x in range(1,101):
    if (x%10==0):
        print("coding dojo")
        continue
    elif(x%5==0):
        print("dojo")
        continue
    else:
        print(x)

# Punto 3

y=0
for x in range(0,500001):
    if (x%2!=0):
        y=y+x
    if(x==500000):
        print(y)
    else:
        continue
    

# Punto 4

for x in range(2018,0,-4):
    print(x)

# Punto 5
lowNum=2
highNum=9
mult=3
for x in range(lowNum,highNum+1):
    if(x%mult==0):
        print(x)

