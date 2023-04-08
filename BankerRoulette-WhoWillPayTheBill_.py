# Banker Roulette - Who will pay the bill ?
import random

name_string = input("Give me everybody's names, seperated by comma.\n")
names = name_string.split(", ")  #Converts separated by comma string to list

print(names)
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = (names[random_choice])
# person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy meal today. ")
