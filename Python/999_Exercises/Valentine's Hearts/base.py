import datetime
import random

thislist = []
thislist2 = []

with open('People.txt') as f:
    for line in f:
        l = line.strip()
        thislist.append(l)

with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        thislist2.append(l)
        
num_people = random.randrange(0,len(thislist))
num_comp = random.randrange(0,len(thislist2))

print(thislist[num_people]+ " " + thislist2[num_comp])