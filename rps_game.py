import random
print("🎮 Rock papermScissors Game")
choices=["rock", "paper", "Scissors"]
computer=random.choice(choices)
user=input("enter rock,paper,or scissors: ").lower()
print("computer chose:",computer)
if user==computer:
    print("it's tie!")
elif user=="rock":
    if computer=="Scissors":
        print("you win!")
    else:
        print("you lose!")
elif user=="paper":
    if computer=="rock":
        print("you win!")
    else:
        print("you lose!")
elif user=="scissors":
    if computer=="paper":
        print("you win!")
    else:
        print("you lose!")
else:
    print("Invlaid input")
    