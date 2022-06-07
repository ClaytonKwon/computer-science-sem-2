print("Please select operation +, -, *, /")
  
  
op = input("Select operations 1, 2, 3, 4 : ")
op = int(op)
  
num1 = input("first number: ")
num1 = int(num1)
num2 = input("second number: ")
num2 = int(num2)

if op == 1:
    print(num1, "+", num2, "=", num1 + num2)
    
elif op == 2:
    print(num1, "-", num2, "=", num1 - num2)
  
elif op == 3:
    print(num1, "*", num2, "=", num1 * num2)
  
elif op == 4:
    print(num1, "/", num2, "=", num1 / num2)

else:
    print("Invalid input")