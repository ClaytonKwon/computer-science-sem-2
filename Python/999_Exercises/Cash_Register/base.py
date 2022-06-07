choice = int(input("how many items would you like?: "))

c = 0 
x = 0

for x in range(0,choice):
    item = input("what item?: ")
    price = int(input("price of item?: "))
    choice = choice + 1 
    c = c + price

print(c)
    