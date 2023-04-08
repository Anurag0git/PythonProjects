print("Welcome to the rollercoaster !")
height = int(input("What is your height in cm ?\n"))

if height >= 120:
  print("You can ride !!")

  age = int(input("What is your age in years \n"))

  if age < 12:
    bill = 5
    print("Child Tickets are $5.")
  elif 12 <= age < 18:
    bill = 7
    print("Youth Tickets are $7.")

  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us !")

  else:
    bill = 12
    print("Adult Tickets are $12.")

  pics = input("Do you want photos? (Y/N)\n")  # if Y (+$3)
  if pics == "Y":
    bill += 3

  print(f"Your total bill is ${bill}.")
else:
  print("Sorry, you have to grow taller before you can ride.  ")
