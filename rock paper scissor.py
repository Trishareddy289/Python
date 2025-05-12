import random

choices=("stone", "paper",  "scissor")
user_choices=input("stone ,paper, or scissor")
computer_choices= random.choice(choices)
print("computer_choice is",computer_choices)
if user_choices==computer_choices:
 print("its tie")
elif (user_choices=="paper" and computer_choices==scissor) or (user_choices=="rock" and computer_choices=="paper") or(user_choices=="scissor" and computer_choices=="rock"):
  print("computer win")
else:
  print("you win !")