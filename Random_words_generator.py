## RANDOM WORDS GENERATOR!!!

import random





# While True loop is used for the programm run into a loop until the user input a valid number. Once the user input a valid number the loop is terminate!!
while True:

    # The open() statement just open the text file and "r" keyword read it.
    with open('/home/sourabh/PythonProjects/RandomData.txt','r') as file:


    # Here the saperated_words variable store that words which are splited by splitlines()method which is used to split the string into list of lines!!
        saperated_words = file.read().splitlines()


    # random.sample()method is used to fetch the words randomly!!
    # Here I used the random.sample()method because I wants to get random words more than 1 !!
    # If you have to get only 1 random word then you can use the random.choice()method!!

    # Ask to user for input that how many random words he/she wanted to fetch!!
    number_of_words = int(input("Enter a number:- "))

    

    # Here I just put the condition that if the number given by user is greter then the actual number of words present in the file then show an warning!!
    if number_of_words > len(saperated_words):
        print("The file does't contain enough words")

    # Here one another condition is that if the user input the numbers of words he/she wanted to randomly fetch is must be greter then 1 other wise they gote an warning for that!!
    elif number_of_words < 2:
        print("Please enter the number greter then 1")
    
    
    else:
        
        # random.sample()method is used to fetch the words randomly!!
        # Here I used the random.sample()method because I wants to get random words more than 1 !!
        # If you have to get only 1 random word then you can use random.choice()method!!
        random_words = random.sample(saperated_words,number_of_words)

        print(random_words)

    break
