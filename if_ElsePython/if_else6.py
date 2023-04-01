# Q.A shop will give discount of 10% if the cost of purchesd quantity is more than 1000
# Ask user for quantity 
# Suppose one unit will cost 100.
#judge and print total cost for user.

purchased_quantity = int(input("Enter quntity:- "))

if purchased_quantity>1000:
    print("You got the discount of 10%")
    print("cost is ",(purchased_quantity*100)-(purchased_quantity*100*.1))
    
else:
    print("You are not eligible for discount")
