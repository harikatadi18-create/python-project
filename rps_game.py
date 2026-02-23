import random

print("🎮 Rock Paper Scissors - Best of 3")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

for round in range(1, 4):
    print(f"\nRound {round}")
    
    computer = random.choice(choices)
    user = input("Enter rock, paper, or scissors: ").lower()

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif user == "rock" and computer == "scissors":
        print("You win this round! 🎉")
        user_score += 1
    elif user == "paper" and computer == "rock":
        print("You win this round! 🎉")
        user_score += 1
    elif user == "scissors" and computer == "paper":
        print("You win this round! 🎉")
        user_score += 1
    elif user in choices:
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("Invalid input!")

print("\nFinal Score:")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print("🏆 You are the overall winner!")
elif computer_score > user_score:
    print("💻 Computer is the overall winner!")
else:
    print("🤝 It's a tie match!")