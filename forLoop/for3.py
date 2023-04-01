# Q.Write a program that appends the square of each number to a new list.

x = [2,3,4,5,6,7,8]
z = []
for i in range(len(x)):
    z.append(x[i]**2)
print("Result: ",z)