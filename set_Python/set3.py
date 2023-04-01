# Q.Write a Python program to remove an item from a set if it is present in the set.

#Create a new set
num_set = set([0, 1, 2, 3, 4, 5])

print(num_set)
print("Remove 0 from the set:")
num_set.discard(4)
print(num_set)
print("Remove 5 from the  set:")
num_set.discard(5)
print(num_set)
print("Remove 2 from the  set:")
num_set.discard(5)
print(num_set)
print("Remove 7 from the  set:")
num_set.discard(15)
print(num_set)
