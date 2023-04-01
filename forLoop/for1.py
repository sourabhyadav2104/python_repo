# Q.Write a program in Python to reverse a word..
str = input("Enter an word:- ")

for i in range(len(str)-1,-1,-1):
    print(str[i],end="")
print("\n")    