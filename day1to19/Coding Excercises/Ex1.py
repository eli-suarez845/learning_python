# Your task is to create a program that generates a random whole number

import random

# Get two numbers from the user and convert them to integers
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# Pick a random int using randint()
rand = random.randint(lower_bound, upper_bound)

print(rand)

