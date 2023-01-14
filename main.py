import random

user_wins = 0
computer_wins = 0

signs = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in signs:
        continue

    random_number = random.randint(0,2) # 0 for rock, 1 for paper, 2 for scissors
    computer_guess = signs[random_number]
    print("computer picked", computer_guess + ".")
    
    if user_input == "rock" and computer_guess == "scissors":
        print("You won!")
        user_wins += 1 

    elif user_input == "paper" and computer_guess == "rock":
        print("You lost!")
        user_wins += 1

    elif user_input == "scissors" and computer_guess == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You")
        computer_wins += 1
        continue
print("Your score is", user_wins)
print("The computer score is", computer_wins)

if computer_wins > user_wins:
    print("Good luck next time! You lost the game.")

if user_wins > computer_wins:
    print("Good game! You won the game.")

if user_wins == computer_wins:
    print("The game is tied.")