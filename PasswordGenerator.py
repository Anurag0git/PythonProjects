letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# num_letters = len(letters)

symbols = [
  '!', '@', '#', '$', '%', '&', '^', '*', '(', ')', '-', '_', '=', '+', '-',
  '/', ',', '.', '?', '/', ':', '<', '>', '[', ']', '{', '}'
]

# num_symbols = len(symbols)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to All-Password Generator!")
no_of_letters = int(
  input("How many letters would you like in your password ?\n"))
no_of_numbers = int(
  input("How many numbers would you like in your password ?\n"))
no_of_symbols = int(
  input("How many symbols would you like in your password ?\n"))

import random

password_list = []

for char in range(1, no_of_letters + 1):
  # rand_letter = random.choice(letters)
  a = random.randint(0, 53)
  rand_letter = letters[a]
  password_list += rand_letter

for char in range(1, no_of_numbers + 1):
  # rand_num = random.choice(numbers)
  b = random.randint(0, 9)
  rand_num = numbers[b]
  password_list += rand_num

for char in range(1, no_of_symbols + 1):
  # rand_symb = random.choice(symbols)
  c = random.randint(0, 28)
  rand_symb = symbols[c]
  password_list += rand_symb

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password if : {password}")
