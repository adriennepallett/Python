# File: passw0rd_Adrienne.py
# Project: CSIS 2101 Assignment 10
# Author: Adrienne Pallett
# History: Version 10.1 November 13, 2022

# Input & Output Files
# Password Checker

'''
Criteria:
    >= 10 characters
    Exactly 3 Uppercase Letters
    Exactly 2 digits
    Exactly 1 special character $ ! or %
    No spaces
    remaining characters all lower case letters
'''

def main():
    # Files
    pass_in = open("passwd_in.txt","r")
    pass_out = open("Adrienne_psswd_out.txt","w")

    # Read Lines
    password = pass_in.readline()

    # While Loop to read all lines
    while password != "":
        password = password.strip("\n")
        print(password)

        # Read the next line
        password = pass_in.readline()

        # Write the output into the output file
        pass_out.write(check_password_Adrienne(password))

    # Close the files
    pass_out.close()
    pass_in.close()


def check_password_Adrienne(password):

    # Character Counters
    low_count = 0
    upper_count = 0
    digit_count = 0
    spec_count = 0
    space_count = 0

    lngth = len(password)

    # Step Counter for characters that meet criterion
    for i in password:
        if i.islower():
            low_count += 1
        elif i.isupper():
            upper_count += 1
        elif i.isdigit():
            digit_count += 1
        elif i == " ":
            space_count += 1
                #   .ISSPACE() DOESNT FUNCTION -- " " USED INSTEAD
        else:
            if i == "$" or i == "!" or i == "%":
                spec_count += 1
                
    # Password Accepted
    if lngth >= 10 and low_count > 0 and upper_count == 3 and digit_count == 2 and spec_count == 1 and space_count == 0:
        msg = f"\n{password} \nPassword Accepted\n"
        return msg

    # Password Doesnt Meet Guidelines
    else:
        msg = f"\n{password} \nPassword not accepted because of the following reasons:"

        # Reason it did not meet the guidelines
        if lngth < 10:
             msg += "\n \t-- Password should be 10 characters or more \n"
        if low_count < 0:
            msg += "\n \t-- Password should contain at least 1 lower case letter \n"
        if upper_count != 3:
            msg += "\n \t-- Password should contain EXACTLY 3 upper case letters \n"
        if digit_count != 2:
            msg += "\n \t-- Password should contain EXACTLY 2 numbers \n"
        if spec_count != 1:
            msg += "\n \t-- Password should contain EXACTLY 1 spacial character: $ ! % \n"
        if space_count > 0:
            msg += "\n \t-- Password should contain no spaces \n"
        
        return msg


if __name__ == "__main__":
    main()
