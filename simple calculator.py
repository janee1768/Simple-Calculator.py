#Simple Calculator

Num_1 = int(input("Enter first number: "))
Num_2 = int(input("Enter second number: "))
operation = input("Enter operation(+,-,*,/): ")
if operation == "+":
    print(Num_1 + Num_2)
elif operation == "-":
    print(Num_1 - Num_2)
elif operation == "*":
    print(Num_1*Num_2)
elif operation == "/":
    print(Num_1/Num_2)
else:
    print("Invalid operation")
    
# This code is a simple calculator that performs basic arithmetic operations.


