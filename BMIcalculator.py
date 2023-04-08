# BMI = Weight(kg) / (height(m))^2
# bmi<18.5 = underweight
# 25>bmi>18.5 = normalweight
# 30>bmi>25 = overweight
# 35>bmi>30= obese
# bmi>35 = clinically obese

print("Wlecome to BMI Calculator !!")
weight = float(input("Please enter your weight (kg):\n"))
height = float(input("Please enter your height (m):\n"))
bmi = round((weight) / (height**2), 2)  # height**2 means height squared
if bmi < 18.5:
  print("You are underweight, since your BMI is ", bmi)
elif bmi < 25:
  print("You are normalweight, since your BMI is ", bmi)
elif bmi < 30:
  print("You are overweight, since your BMI is ", bmi)
elif bmi <= 35:
  print("You are obese, since your BMI is ", bmi)
elif bmi > 35:
  print("You are clinically obese, since your BMI is ", bmi)
