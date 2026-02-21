import random
print("welcome to number guessing game!")
number=random.randint(1,100)
max_attempts=5
for attempt in range(1,max_attempts+1):
    guess =int(input(f"attempt {attempt}/ 5 - enter your guess(1-100): "))
    if guess<number:
        print("too low!Try again")
    elif guess>number:
        print("too high! try again")
    else:
        print("congratulations!!! you guessed it in attempts!")
        break
else:
    print("Game over!the correct number was:",number)
