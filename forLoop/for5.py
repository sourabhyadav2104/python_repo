# Q. Write a program that appends the type of elements from a list.
n = [20,'sourabh',45,89]
x = []
for i in range (len(n)):
    x.append(type(n[i]))
print(n)
print(x)    