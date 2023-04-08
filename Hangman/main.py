import hangman_words
from hangman_art import stages #, logo
# word_list = ["apple", "banana", "grapes", "orange", 'coconut']
import random

# print(logo)

chosen_word = random.choice(hangman_words.word_list)

# print(chosen_word)
# apple
word_len = len(chosen_word)
# 5

lives = 6

display = []

for letter in chosen_word:
  display += "_"
print(display)
# ['_', '_', '_', '_', '_',]

end_of_game = False

while not end_of_game:
  guess = input("guess a letter: ").lower()  # p

  for position in range(word_len):  #range = 5
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  print(display)
  # ['_', 'p', 'p', '_', '_',]

  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Loose !")

  if "_" not in display:
    end_of_game = True
    print("You Win !!")

  print(stages[lives])