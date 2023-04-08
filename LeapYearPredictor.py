'''
on every year that is evenly divisible by 4 
    except every year that is evenly divisible by 100
        unless the year is also divisible by 400


e.g. The year 2000:
2000/4 = 500 (Leap)
2000/100 = 20(not Leap)
2000/400 = 5 (Leap)

The year 2100:
2100/4 = 525 (Leap)
2100/100 =21(Not Leap)
2100/400 = 5.25(Not Leap)


'''

year = int(input("Which year do you want to check ?\n"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap Year")
    else:
      print("Not Leap Year")
else:
  print("Not Leap Year")
