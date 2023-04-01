# Q. Finding the sum of even numbers using while loop.

i = 0
sum = 0
n = int(input("Enter the number n: "))

while  i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
        
print("Sum of even numbers till n:",sum)