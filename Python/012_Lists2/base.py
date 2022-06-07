import random
user = int(input("how many numbers?: "))
thislist = []
for x in range(0,user):
    user1 = int(random.randrange(0,10))
    thislist.append(user1)
print(thislist, end=",")