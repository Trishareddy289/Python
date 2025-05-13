print("k.trisha,USN:1AY24AI051,SEC:M")

import random

n = random.randint(1,100)
while True:
     guess = int(input("guess a number between 1 and 100:"))
     if guess < n:
         print ("too low")
     elif guess > n:
         print("too high!")
     else:
         print("you won!")
         break
