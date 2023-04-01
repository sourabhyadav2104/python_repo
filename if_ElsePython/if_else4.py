# Q.A company decided to give bonus of 50% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter your salary:- "))
servise_year = int(input("Enter your service_year:- "))

if servise_year>5:
    print("Your are eligible for bonus")
    print(salary+salary/100*5)
else:
    print("You are not eligible for bonus")    