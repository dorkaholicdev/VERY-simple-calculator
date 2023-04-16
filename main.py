# Inputs
print("Welcome to Calculation!")
number1 = input("What is your first number?\n")
sign = input("1 - Addition; 2 - Subtraction; 3 - Multiplication; 4 - Division, Which would you like to choose?\n")
number2 = input("What is your second number?\n")

# Number stuff
if (number1.isnumeric() or (number1.startswith('-') and number1[1:].isdigit())) and (number2.isnumeric() or (number2.startswith('-') and number2[1:].isdigit())):
  if sign == '1':
    print(number1, '+', number2, "=", int(number1) + int(number2))
  elif sign == '2':
    print(number1, '-', number2, "=", int(number1) - int(number2))
  elif sign == '3':
    print(number1, '*', number2, "=", int(number1) * int(number2))
  elif sign == '4':
    print(number1, '/', number2, "=", int(number1) / int(number2))
  else:
    print("ERROR: You may have put a value other than a number which caused this")
else:
  print("ERROR: You may have put a value other than a number which caused this")