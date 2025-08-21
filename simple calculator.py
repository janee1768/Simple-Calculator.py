import math

#Simple Calculator


operation = input("Enter operation(+,-,*,/,^,sqrt): ")
Num_1 = int(input("Enter first number: "))
if operation != "sqrt":
    Num_2 = int(input("Enter second number: "))

if operation == "+":
    print(Num_1 + Num_2)
elif operation == "-":
    print(Num_1 - Num_2)
elif operation == "*":
    print(Num_1*Num_2)
elif operation == "/" and num2 != 0:
    print(Num_1/Num_2)
elif operation == "^":
    print(pow(num1,num2))
elif operation == "sqrt" and num1 >= 0:
    print(math.sqrt(num1))
else:
    print("Invalid operation")
    
# This code is a simple calculator that performs basic arithmetic operations.


