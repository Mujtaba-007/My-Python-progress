import random

secret = random.randint(1, 100)  # Generates random number between 1-100
guesses = 0

while True:
    guess = int(input("Guess the number: "))
    guesses += 1

    if guess > secret:
        print("Lower number please!")
    elif guess < secret:
        print("Higher number please!")
    else:
        print(f"Correct! 🎉 You got it in {guesses} guesses!")
        break

### Sample run 
'''
Guess the number: 50
Lower number please!
Guess the number: 25
Higher number please!
Guess the number: 37
Correct! 🎉 You got it in 3 guesses!
'''
