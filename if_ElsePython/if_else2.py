# Q. Write a program to find the lowest number out of two numbers expected from user.
num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))

if num1<num2:
    print(num1," is lowest to ",num2)
elif num1==num2:
    print(num1," is equal to ",num2)
else:
    print(num2," is lowest to ",num1)        

