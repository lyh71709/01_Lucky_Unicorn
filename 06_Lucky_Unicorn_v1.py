# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

# Integer checking function
def intcheck(question, low, high):
    valid = False

    while not valid:
        error = "Whoops! Please enter an integer between {} and {}: ".format(low, high)

        try:
            response = int(input("Enter an integer between {} and {}: ".format(low, high)))
            if low <= response <= high:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

# main routine goes here

keep_going = ""
while keep_going == "":

    how_much = intcheck("How much money do you want to play with? ", 1, 10)
    print("You have chosento play with ${}".format(how_much))

    keep_going = input("Press <Enter> to keep going or any key to quit. ")