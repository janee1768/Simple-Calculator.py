#Simple Calculator

Num_1 = int(input("Enter number: "))

operation = input("Enter operation(+,-,*,/,^2): ")

if operation in ['+','-','*','/']:
   Num_2 = int(input("Enter 2nd number: "))
while True:
    #Taking square of the number

  if operation == "^2":
    Num_1 = Num_1 ** 2 
    print("Answer: ",Num_1)
    break

    # Taking sum of the 2 numbers 

  elif operation == "+":
        Num_1 += Num_2 
        print("Answer: ",Num_1)
        break

    # Taking the difference between  2 numbers

  elif operation == "-":
        Num_1 -= Num_2 
        print("Answer: ",Num_1)
        break 

    # Multiplying both numbers 

  elif operation == "*":
        Num_1 *= Num_2 
        print("Answer: ",Num_1)
        break 

    
    # Dividing both numbers 

  elif operation == "/":
      try:
          Num_1 /= Num_2 
          print("Answer: ",Num_1)

      except ZeroDivisionError :
          print("Dividing by zero is not allowed!.")

      break 
  else: 
      print(" Invalid operation use following (+,-,*,/,^2)")
      break 
        
#End 
    

