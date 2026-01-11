#rock,paper,scissors game using Python.
import random

opt = ["Rock", "Paper", "Scissors"]
a = input("choose Rock, Paper or Scissors:")
b = random.choice(opt)

print("You chose: ", a)
print("Computer chose:", b)
if a not in opt:
    print("Invalid choice. Pick one from options")
else:
    if a == b:
        print("Tie")
    elif (a == "Rock" and b == "Paper") or (a == "Scissors" and b == "Rock") or (a == "Paper" and b == "Scissors"): 
        print("You lose")
    else:

        print("You win")
