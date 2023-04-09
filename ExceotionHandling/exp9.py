
while True:
    try:
        email = input("Enter your email address: ")
        if not email.endswith("@gmail.com"):
            raise ValueError("Invalid email address. Please enter a valid Gmail address.")
        email_without_at = email.replace("@", "")
        print("Your email without '@':", email_without_at)
        break
    except ValueError as error:
        print(error)
