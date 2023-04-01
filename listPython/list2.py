# Q.Concatenate two lists index-wise.

list1 = ["M", "na", "i", "sou"] 
list2 = ["y", "me", "s", "rabh"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)