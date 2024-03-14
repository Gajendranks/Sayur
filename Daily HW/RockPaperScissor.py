

import random

options = ["Rock", "Paper", "Scissors"] 
count = 0

for _ in range(3):
    user = input("Enter Rock, Paper, or Scissors: ")
    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        print("You win this round!")
        count += 1
    else:
        print("Computer wins this round!")

if count > 1:
    print("You won best of three!")
else:
    print("Computer won best of three!")
