# Q Write a Python script to merge two Python dictionaries.

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
a = d1.copy()
a.update(d2)
print(a)