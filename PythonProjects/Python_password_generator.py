## PASSWORD GENERATOR

import random
import string

def generate_password(length):
    """
    Generates a random password of the specified length using
    ASCII lowercase letters, ASCII uppercase letters, ASCII digits,
    ASCII hexadecimal digits, ASCII octal digits, and ASCII punctuation.
    """
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.hexdigits + string.octdigits + string.punctuation

    # The random.choice function choose the characters for password and concatenate the characters into string by using the join method.
    password = ''.join(random.choice(characters) for i in range(length))

    return password

while True:
    try:
        # Take input from user for password length
        password_length = int(input("Enter the password length:- "))

        # Generate password of the desired length
        password = generate_password(password_length)

        # Print the generated password
        print("Your password is:", password)

        # Exit the loop
        break

    except ValueError:
        # Handle invalid input by prompting the user to try again
        print("Invalid input. Please enter a positive integer for the password length.")
        continue
