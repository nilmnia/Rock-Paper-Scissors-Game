import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors!")
print("The game has 3 rounds.")

for round in range(1, 4):

    print("\nRound", round)

    user = input("Choose rock, paper or scissors: ").lower()

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    if user == computer:
        print("It's a tie!")

    elif user == "rock" and computer == "scissors":
        print("You win this round!")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("You win this round!")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

print("\n----- Final Result -----")

if user_score > computer_score:
    print("Congratulations! You won the game!")

elif computer_score > user_score:
    print("Computer won the game!")

else:
    print("The game ended in a tie!")

print("Your final score:", user_score)
print("Computer final score:", computer_score)
