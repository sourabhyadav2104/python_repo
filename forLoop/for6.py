# Q.Write a program to filter even and odd number from a list.

x = [10,20,35,65,78,90]
eve = []
odd = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        eve.append(x[i])
    else:
        odd.append(x[i])
print("Even numbers are: ",eve)
print("Odd numbers are: ",odd)