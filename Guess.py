import random

answer = random.randint(1, 100)
guess = int(input("Guess a number (1-100): "))

if guess == answer:
    print("Correct!")
elif guess < answer:    
    print("Too low! The answer was", answer)
else:
    print("Too high! The answer was", answer)
