## CONVERT AN PLAIN TEXT TO ENCRYPTED TEXT!!

def encrypt(text, formula):
   
    encrypted_text = ""
    for char in text:

        ## The char.isalpha()method is check whether the character is alphabate or not!!
        if char.isalpha():
            ## The char.islower()method is used here to check that the alphabate is in lowercase!!
            if char.islower():
                encrypted_char = chr((ord(char) - 97 + int(eval(formula))) % 26 + 97)

            ## If the aplhabate is not lowercase then else part assume that the given character is an Uppercase character!!    
            else:
                encrypted_char = chr((ord(char) - 65 + int(eval(formula))) % 26 + 65)

        ## The char.isdigit()method check that the character is an digit or not!!
        elif char.isdigit():
            # Shift digits by formula + 5 in my case but you can change it according to you!!
            encrypted_char = chr((ord(char) - 48 + int(eval(formula)) + 5) % 10 + 48)

        ## Here if the character is from "!@#$%^&*()" it then shift perform accordingly
        elif char in "!@#$%^&()":
            # Here I just  Shift special characters by formula + 10 in my case you can change it according to you!!
            encrypted_char = chr((ord(char) - 33 + int(eval(formula ))+ 10) % 15 + 33)

        ## Leave other characters unchanged!! 
        else:
              encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text


# Ask input from user
text = input("Enter the text to encryption:- ")
formula = input("Enter the formula for encryption:- ")



# Call encrypted_text() function with user input
encrypted_text = encrypt(text, formula)

# Print the encrypted text
print("Encrypted Text:- ", encrypted_text)

