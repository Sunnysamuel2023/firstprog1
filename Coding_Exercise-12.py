import random

names = input("Enter the names separated by commas: ")
name_list = names.split(",")

bill = random.choice(name_list)
print(f"{bill} will pay the bill")

