import random #Importing the random module.

number = random.randint(1, 10) #Setting a random int value.
guess = 0 #Setting a value that is outside the range of the random.randint(1, 10).

print("Guess a number between 1 and 10.") #Printing an instruction.

while guess != number: #Opening a while loop.
    guess = input("Enter guess: ") #Printing an instruction.

    try: #Opening a try-except block to catch the value error that accrues with invalid input.
        guess = int(guess)
    except ValueError:
        print("Invalid input, please try again.")
        continue

    if(guess < number): #Checking if the guessed number is lower than the generated number.
        print("Too low, guess higher!")
    elif(guess > number): #Checking if the guessed number is higher than the generated number.
        print("Too high, guess lower!")
    else: #If the guessed number is not lower or higher than the generated number, then is the right number.
        print("You have guessed the number. Bravo!")

    while guess == number: #Opening a while loop so the game can be replayed.
        play_again: str = input("Play again? (y/n): ").lower() #.lower() method is used , so the following logic works as intended.

        if play_again == "y": #Checks if the input is positive, and if so, resets the variables.
            print("Guess a number between 1 and 10.")
            guess = 0
            number = random.randint(1, 10)
        elif(play_again == "n"): #Checks if the input is negative, and if so, breaks out of the loop.
            print("Okay, goodbye!")
            break
        else:
            print("Invalid input, please try again.") #Catches invalid input.