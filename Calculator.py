print("Hello World!\n\nThis is my first program\nThe calculator:)\n")
a = (int(input("Please Enter the first number: ")))
b = (int(input("Enter the second number: ")))
c = (input("Enter the Operation '+, -, *, /, % ': "))

if c == '+':
  print("Answer =", a + b)

elif c == '-':
  print("Answer =", a - b)

elif c == '*':
  print("Answer =", a * b)
elif c == '/':
  print("Answer =", a / b)

elif c == '%':
  print("Answer =", a % b)
