import random

letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
          'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '+', '-']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("Welcome to password generator")
n_letter = int(input("How many character would you like to print in your Password: "))
n_symbol = int(input("How many Symbol would you like to print in your Password: "))
n_number = int(input("How many numbers would you like to print in your Password: "))

password_list = []
for i in range(1, n_letter+1):
    char = random.choice(letter)
    password_list += char

for i in range(1, n_number):
    num = random.choice(number)
    password_list += num

for i in range(1, n_symbol):
    sym = random.choice(symbol)
    password_list += sym

random.shuffle(password_list)  # to shuffle the list
#print(password_list)
password = ''
for char in password_list:
    password += char
print("THis is your Generated Password: ", password)

