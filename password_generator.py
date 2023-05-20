import random

print("Welcome to PyPassword generator\n")
alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
no_alphabets = int(input("Enter no of alphabets you want:"))
no_numbers = int(input("Enter no of numbers you want:"))
no_symbols = int(input("Enter no of symbols you want:"))
password_list = []
for char in range(1, no_alphabets):
  password_list += random.choice(number)
for char in range(1, no_numbers):
  password_list += random.choice(alphabet)
for char in range(1, no_symbols):
  password_list += random.choice(symbol)

random.shuffle(password_list)

password = ""
for i in password_list:
  password += i

print(f"Your password is: {password}")