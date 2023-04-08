# Caeser cipher

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", ",", ".", "?"
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(normal_text, shift_num):
  cipher = ""
  for letter in normal_text:
    position = alphabet.index(letter)
    new_position = position + shift_num
    if new_position > 29:
      new_new_position = new_position - 30
      new_letter = alphabet[new_new_position]
      cipher += new_letter
    else:
      new_letter = alphabet[new_position]
      cipher += new_letter
      print(cipher)


def decrypt(encrypted_text, shift_num):
  cipher = ""
  for letter in encrypted_text:
    position = alphabet.index(letter)
    new_position = position - shift_num
    if new_position < 0:
      new_new_position = 30 + new_position
      new_letter = alphabet[new_new_position]
      cipher += new_letter
    else:
      new_letter = alphabet[new_position]
      cipher += new_letter
  print(cipher)


if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)