# Q. Finding the sum of numbers in a list using while loop

myList = [23,45,12,10,25]
i = 0 
sum = 0

while i < len(myList):
    sum += myList[i]
    i += 1

print(sum)