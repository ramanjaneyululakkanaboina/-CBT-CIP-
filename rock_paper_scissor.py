import random
choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
my_choice = input("Enter your choice (rock, paper, scissors): ").lower()

if my_choice not in choices:
    print("Invalid input! Please enter one of: Rock, Paper, Scissors.")
else:
    print(f"Computer Choice: {computer}, Your Choice: {my_choice}")

    if computer == my_choice:
        print("It's a tie!")
    elif (my_choice == 'rock' and computer == 'scissors') or \
         (my_choice == 'scissors' and computer == 'paper') or \
         (my_choice == 'paper' and computer == 'rock'):
        print("You Win! 🎉")
    else:
        print("Computer Wins! 😢")
