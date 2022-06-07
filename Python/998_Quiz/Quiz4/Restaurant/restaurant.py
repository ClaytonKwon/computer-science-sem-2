import random

thislist = ["restraunt1", "restraunt2", "restraunt3"]
restraunt1m = ["food", "foood", "fooood"]
restraunt2m = ["food1", "foood1", "fooood1"]
restraunt3m = ["food2", "foood2", "fooood2"]
print(thislist)
person = input("pick a retraunt: ")

if person == "restraunt1":
    print(restraunt1m)
    print("suggested" + " " + restraunt1m[random.randrange(0,3)])

if person == "restraunt2":
    print(restraunt2m)
    print("suggested" + " " + restraunt2m[random.randrange(0,3)])
    
if person == "restraunt3":
    print(restraunt3m)
    print("suggested" + " " + restraunt3m[random.randrange(0,3)])

elif person != thislist:
    print("not real...")
