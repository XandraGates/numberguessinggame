#Guess the number game is Python
import random
print("Welcome to the number guessing game. Please enter your name.")
name = input()

if name == "":
    print("So, you don't want to tell me your name...")
    print("A wise choice. But now I will have to use something generic...")
    print("Like buddy.")
    print("And if you don't like buddy, then tough.")
    print("That's what you get for not answering a simple question.")
    name = "buddy"

print("Hello there " + name + "! It is time for you to guess a number between 1 and 20.")
print("You will be given six attempts to guess the correct number.")
print("Please make your first guess.")
secretNum = random.randint(1, 20)
guess = input()

#ask player to guess 6 times
for i in range(1, 6):
    chances = 6 - i
    try:
        if int(guess) > 21 or int(guess) < 1 :
            print("Did you not read the instructions?")
            print("You're supposed to guess a number between 1 and 20...")
            print("If you want to continue putting in silly numbers, that's your choice.")
            print("But don't blame me when you run out of guesses.")
            print("You have " + str(chances) + " guesses left.")
            guess = input()
        elif int(guess) < secretNum:
            print("Your guess was too low. Please try again.")
            guess = input()
        elif int(guess) > secretNum:
            print("Your guess was too high. Please try again.")
            guess = input()
        else:
            break
    except:
        print("Invalid guess. Make sure you are entering a number!")
        print("You have " + str(chances) + " guesses left.")
        guess = input()

if int(guess) != secretNum:
    print("Unlucky " + name + "! Looks like you're out of attempts")
    print("The number I was thinking of is " + str(secretNum))
if int(guess) == secretNum:
            print("Congratulations " + name + "! You guessed correctly!")
            print("Number of guesses: " + str(i))
