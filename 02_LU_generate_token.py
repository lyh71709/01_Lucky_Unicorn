# Lucky Unicorn Decomposition Step 2
# Generate a random token

# To do
# Set up starting amount
# Choose 100 tokens (ie: play 100 rounds and...
#   count # of unicorns and multiply by 5
#   count # of horse/zebra and multiply by 0.5
#   count # of donkeys
# work out total won / lost


import random

HOW_MUCH = 100
tokens = ["Horse", "Zebra", "Donkey", "Unicorn"]

for item in range(0,HOW_MUCH):

    chosen = random.choice(tokens)

    print(chosen)

