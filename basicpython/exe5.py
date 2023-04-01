#6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. 

numbers = input("Enter any sequence of numbers: ")
list = numbers.split(",")
tuple = tuple(list)
print(list)
print(tuple)