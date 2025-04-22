secret = 6

guess = int(input("Enter a number between 1 and 10: "))

if guess > secret:
    print("Your number is above the secret number")
elif guess < secret:
    print("Your number is below the secret number")
else:
    print("You have guessed right!")