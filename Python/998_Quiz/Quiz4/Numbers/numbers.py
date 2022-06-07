num = [6,9,32,28,15,22,3,18]

sum1 = 0 

for x in range(0, len(num)):
    sum1 = sum1 + num[x]
    
ave = sum1 / len(num)
maxV = num[0]
minV = num[0]



for x in num:
    if x > maxV:
        maxV = x
    if x < minV:
        minV = x
        
print(minV)
print(maxV)
print(ave)