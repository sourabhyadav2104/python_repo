
while True:
    try:
        a = 10
        b = int(input("Enter a number: "))
        if b == 0:
            raise ValueError
        c = a/b
        print(c)
        break
    except ZeroDivisionError:
        print("Division by zero not allowed")
    except ValueError:
        print("Invalid input. Please enter a non-zero integer.")
