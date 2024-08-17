size = input("Please Enter Size of your Pizza (S/M/L):")
bill = 0
if size == 's' or size == 'S':
    bill = 100
    print("You have selected Small Size Pizza")
elif size == 'm' or size == 'M':
    bill = 200
    print("You have selected Medium Size Pizza")
else:
    bill = 300
    print("You have selected Large Size Pizza")
want_pep = input("Do you want Pepperoni (Y/N):")
if want_pep == 'y' or want_pep == 'Y':
    if size == 's' or size == 'S':
        bill = bill + 30
        print("You have added Pepperoni")
    else:
        bill = bill + 50
        print("You have added Pepperoni")
extra_cheese = input("Do you want Extra Cheese (Y/N):")
if extra_cheese == 'y' or extra_cheese == 'Y':
    bill = bill + 20
else:
    print()

print(f"Your total bill is {bill}")
