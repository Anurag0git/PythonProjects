print("Welcome to the Tip Calculator !\n")
bill = float(input("What was the total bill (in Rs) ?\n"))
tip = int(input("What percentage of the tip would you like to give ?; 10, 12 or 15 \n:" ))
final_tip = float(bill * (tip/100))
bill_split = int(input("How many people to split the bill ?\n"))
final_bill = round(((bill + final_tip) / bill_split), 2)        #round dataType is used to round off final bill upto 2 decimal places
print(f"Each person should pay :Rs.{final_bill}")    