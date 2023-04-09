
def divide(x, y):
	try:
		result = x / y
		print( result)
	except ZeroDivisionError:
		print("Error ! You are dividing by zero ")
		
divide(3, 2)
