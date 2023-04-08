# Rock, Paper, Scissors !
import random

user_choice = int(
  input(
    "What do you choose?\nType 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
comp_choice = random.randint(0, 2)
print(f"Computer chose {comp_choice}")
choices = [user_choice, comp_choice]

if choices == [0, 2] or choices == [1, 0] or choices == [2, 1]:
  print("You Win !!")
elif choices[0] == choices[1]:
  print("Draw.")
else:
  print("You Loose !")
