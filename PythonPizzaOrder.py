'''
SMALL PIZZA = 15
MEDIUM PIZZA = 20
LARGE PIZZA = 25
PEPPR. FOR SMALL = +2
PEPPR. FOR MED. AND LARGE = +3
EXTRA CHEESE FOR ANY SIZE = +1
'''

print("Welcome to Python Pizza Deliveries !")
size = (input("What size do you want ? S, M or L ?\n"))
add_pepproni = (input("Do you want Pepperoni ? (Y/N)\n"))
extra_cheese = (input("Do you want extra cheese ? (Y/N)\n"))
s = 15
m = 20
l = 25
a = (add_pepproni == "Y")
b = (extra_cheese == "Y")
'''
if size == "S":
    if a == True and b == False:
        print("Your Final Bill is: $", s+2)
    elif a == False and b == True:
        print("Your Final Bill is: $", s+1)
    elif a == True and b == True:
        print("Your Final Bill is: $", s+3)
    elif a == False and b == False:
        print("Your Final Bill is: $", s)
elif size == "M":
    if a == True and b == False:
        print("Your Final Bill is: $", m+3)
    elif a == False and b == True:
        print("Your Final Bill is: $", m+1)
    elif a == True and b == True:
        print("Your Final Bill is: $", m+4)
    elif a == False and b == False:
        print("Your Final Bill is: $", m)
elif size == "L":
    if a == True and b == False:
        print("Your Final Bill is: $", l+3)
    elif a == False and b == True:
        print("Your Final Bill is: $", l+1)
    elif a == True and b == True:
        print("Your Final Bill is: $", l+4)
    elif a == False and b == False:
        print("Your Final Bill is: $", l)        
else:
    print("Your input is invalid.")'''

# UPDATED CODE
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepproni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
if extra_cheese == "Y":
  bill += 1

print(f"Your Final bill is ${bill}")
