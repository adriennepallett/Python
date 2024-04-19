# File: For_Loop_Adrienne.py
# Project: CSIS 2101 Assignment 4
# Author: Adrienne Pallett
# History: Version 4.1 September 21, 2022

# Series of For and While Loops

# Loop 1 - Count Down
# For Loop that counts down from 24 to 13
# Displays each value in the loop

def for_while_loop_Adrienne():
    
    # Loop 1 - Count Down
    # For Loop that counts down from 24 to 13
    # Displays each value in the loop on a single line with ending period
    
    for i in range (24,12,-1): ## (24,13,-1)
        print(i, end=" ")
    print(".") ## Adds a space. f"{13}."

    print("End of Loop 1")
    print ()

    
    # Loop 2 - Count by 9
    # For Loop that counts from 9 to 81 by 9 separated by comma

    for n in range (9,82,9):

        if n == 81:
            print (n, end=" ")
        else :
            print (n, end = ", ")

    print ()
    print ("End of Loop 2")
    print ()
    

    # Loop 3 - Assignment Prints
    # While Loop printing a statement
    # Prints statement based on user input of number of prints
   
    counter = 0
    n = int(input("Enter number of prints: "))
    
    while counter < n:
        k = counter + 1
        print ("I am working on assignment ", k)
        ## missing a "."
            ## print (f"I am working on my assignment {k}.")
        
        counter = counter + 1

    print ("End of Loop 3")
    print ()
    
    
    # Loop 4 - Even/Odd Countdown
    # While Loop counting down from an integer input

    value = int(input("Enter Starting Point: "))
    counter = 1
    if value % 2 == 0:
        value = value + 1 ## or value +=1
    
    while counter <= value:
        print(value, end=" ")
        value -= 2
        
    print () ## blank print statment breaks while loop always
    print ("End of Loop 4")
    print ()
    

    # Loop 5 - Count Up Evens & Odds
    # For Loop that counts from 0 to highest even digit within values
    # Sequential even,odd with have same output
    
    digit = int(input("Please Enter Stopping Point: "))

    for i in range (0, digit, 2):
        print (i, end=" ")
    print ()
    print ("End of All Loops")

    print ()
    print ("This completes my Assignment 4")
    
for_while_loop_Adrienne()
