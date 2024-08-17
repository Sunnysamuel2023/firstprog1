number = int(input("Enter a number (Press 0 to Quit): "))
total = 0

while number != 0:
    total += number
    print("Now the total is : ", total)
    number = int(input("Enter a number (Press 0 to Quit): "))
else:
    print("You have entered 0, Bye Bye loop")
