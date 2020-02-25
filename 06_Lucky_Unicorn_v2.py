# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability
# Post usability, harder to get a unicorn

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

# Appropriate Introduction to the game itself and a brief explanation of how it works
print()
print("*******Welcome to the Lucky Unicorn Game!*******")
print("This game was created to raise money for charity")
print()
print("So input a certain amount of money to begin playing")
print("Each round cost $1 to play and depending on the token is how much you won back")
print("The four different tokens are worth different amounts of money")
print("A Unicorn is worth $5, a Zebra is worth 50c, a Horse is worth 50c as well and a Donkey is worth nothing. ")
print()

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money do you want to play with(Must be between $1 and $10)? $", 1, 10)

keep_going = ""
while keep_going == "":

    # generate a number between 1 and 100 to assign tokens...
    token_number = random.randrange(1,100)

    if token_number <= 7:
        token="Unicorn"
    elif 8 < token_number <= 30:
        token = "Horse"
    elif 31 < token_number <= 55:
        token = "Zebra"
    else:
        token = "Donkey"

    # Randomly choose a token from our list above
    print()
    print()
    print("-" * 20)
    print("You got a {}".format(token))
    print("-" * 20)


    # Adjust total correctly for a given token
    if token == "Unicorn":
        balance += 5
        feedback = "Congratulations you won $5.00"
    elif token == "Donkey":
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
