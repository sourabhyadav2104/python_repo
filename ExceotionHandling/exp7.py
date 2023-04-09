# Program to handle key error:

try:
    mydict = {'a': 1, 'b': 2, 'c': 3}
    print(mydict['d'])
except KeyError:
    print("Key not found")
