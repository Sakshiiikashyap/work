# ------------------------------------------
# Personal Introduction Program
# Author: Your Name
# Description:
# This program asks the user for some basic
# information and displays a friendly
# personalized welcome message.
# ------------------------------------------

# Getting user information
name = input("What is your name? ")
age = input("How old are you? ")
hobby = input("What is your favorite hobby? ")
city = input("Which city do you live in? ")

# Displaying welcome message
print("\n" + "=" * 40)
print("🎉 Welcome! 🎉")
print("=" * 40)

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"You love {hobby}.")
print(f"It's nice to know you're from {city}.")

print("\nHave a wonderful day and keep learning Python! 🚀")