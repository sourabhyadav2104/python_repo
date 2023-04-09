# Q.WAP to separate positive and negative number from a list.

x = [23,4,-6,23,-9,21,3,-45,-8]
pos = []
neg = []
for i in range(len(x)):
    if x[i] < 0:
        neg.append(x[i])
    else:
        pos.append(x[i])
print("Positive numbers are: ",pos)
print("Negative numbers are: ",neg)