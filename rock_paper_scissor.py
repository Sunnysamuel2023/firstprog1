import random
rock = '✊'
paper = '✋'
scissor = '✌️'
game_image = [rock, paper, scissor]
user_choice = int(input("Enter the number between 0 for Rock, 1 for Paper and 2 for Scissor:"))
if (user_choice < 0) and (user_choice <= 3):
    print("You've a entered Invalid Number, you Lose")
else:
    print("Your Choice:")
    print(game_image[user_choice])
    comp_choice = random.randint(0, 2)
    print("Computer's Choice:")
    print(game_image[comp_choice])
    if user_choice == comp_choice:
        print("It's a Draw")
    elif (user_choice == 0) and (comp_choice == 2):
        print("You Win")
    elif (user_choice == 2) and (comp_choice == 0):
        print("You Lose")
    elif comp_choice > user_choice:
        print("You Lose")
    elif user_choice > comp_choice:
        print("You Win")
