#18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
firstNumber = int(input("Enter first number:-"))
secondNumber = int(input("Enter second number:-"))
lastNumber = int(input("Enter last number:-"))

if firstNumber==secondNumber and lastNumber:
    print(3*(firstNumber+secondNumber+lastNumber))
else:
    print("All the numbers are uniqe")    

