import random
lowerNumber = 5
upperNumber = 30
randomNumber = random.randint(lowerNumber, upperNumber)

print("Welcome to my Random Number Guessing Game")
playerguess = int(input("Pick a number between 5 and 30"))

if playerguess == randomNumber:
  print("You win!")
else:
  print(randomNumber)
  print("You lose")