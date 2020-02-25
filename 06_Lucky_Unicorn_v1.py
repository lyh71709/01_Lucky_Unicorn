# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

import random

# Integer checking function
def intcheck(question, low, high):
    valid = False

    while not valid:
        error = "Whoops! Remember it has to be a number and cannot be a decimal. Please enter an amount between ${} and ${}: ".format(low, high)

        try:
            response = int(input(question))
            if low <= response <= high:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

# main routine goes here

# Appropriate Introduction to the game itself and a brief explanation of how it works
print()
print("*******Welcome to the Lucky Unicorn Game!*******")
print("This game was created to raise money for charity")
print()
print("So input a certain amount of money to begin playing")
print("Each round cost $1 to play and depending on the token is how much you won back")
print("The four different tokens are worth different amounts of money")
print("A Unicorn is worth $5, A Zebra is worth 50c, A Horse is worth 50c as well and A Donkey is worth nothing. ")
print()

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money do you want to play with (Must be between $1 and $10)? $", 1, 10)

keep_going = ""
while keep_going == "":

    # Tokens lsit includes 10 items to prevent too many unicorns being chosen
    token = ["Horse", "Horse", "Horse", "Zebra", "Zebra", "Zebra", "Donkey", "Donkey", "Donkey", "Unicorn"]

    # Randomly choose a token from our list above
    chosen = random.choice(token)
    print()
    print("You got a {}".format(chosen))


    # Adjust total correctly for a given token
    if chosen == "Unicorn":
        balance += 5
        feedback = "Congratulations you won $5.00"
    elif chosen == "Donkey":
        balance -= 1
        feedback = "Sorry you didn't win anything this round"
    else:
        balance -= 0.5
        feedback = "Congratulations you lost 50c"

    print()

    print(feedback)
    print("You have ${:.2f} to play with".format(balance))

    # If user has enough money to play, ask if they want to play again...
    if balance < 1:
        print("Sorry you don't have enough money to continue.")
        print("Game Over!")
        keep_going = "end"
    else:
        print()
        keep_going = input("Press <ENTER> to keep playing or any key to quit. ")
        print()

# Goodbye to user when the game ends
print()
print("Thanks for playing!")
