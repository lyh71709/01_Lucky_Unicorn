# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

import random

# Integer checking function
def intcheck(question, low, high):
    valid = False

    while not valid:
        error = "Whoops! Please enter an amount between ${} and ${}: ".format(low, high)

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

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money do you want to play with? ", 1, 10)

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
        feedback = "Congratulations you won 50c"

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
