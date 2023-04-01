#21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
number = int(input("Enter an number:- "))

if number%2==0:
    print(number," is even number")
else:
    print(number," is odd")    