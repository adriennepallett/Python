# File: Adrienne_Assgn6
# Project: CSIS 2101 Assignment 6
# Author: Adrienne Pallett
# History: Version 6.1 October 6, 2022

# This function is the CSIS2101 version of the game rock, paper, scissors

import random

# Game Introduction
print ("If you like Rock Paper Scissors, you'll like this game")
print ("Its Rock Paper Scissors, superhero style")
print ()
print ("You'll pick a superhero, and the the computer will pick a superhero")
print ("Then the two will battle in the cybersphere, and you'll discover the \
winner")
print ()
print ("Available superheros are:")
print ("A for Aqua-Man")
print ("H for Human Torch")
print ("S for Swamp Thing")
print ()


def main ():

    # Character Selection

    Adrienne_user = input("Choose your character: ")
    print ()

    # Character Validation

    counter = 1

    while counter <= 2:
        if Adrienne_user == "a" or Adrienne_user == "h" or Adrienne_user == "s":
            counter += 1
        else:
            print ("This is the wrong universe. Please choose a, h, or s")
            Adrienne_user = input("Choose your character: ")
            counter -= 1
        counter += 1

    # Character Name

    if Adrienne_user == "a": # Should consider A H S
        hero = "Aqua Man"
    elif Adrienne_user == "h":
        hero = "Human Torch"
    else:
        hero = "Swamp Thing"

    # Computer's Selection

    comp_number = random.randrange (9,28,9)

    if comp_number == 9:
        Adrienne_comp = "a"
        villain = "Aqua Man"
    elif comp_number == 18:
        Adrienne_comp = "h"
        villain = "Human Torch"
    else:
        Adrienne_comp = "s"
        villain = "Swamp Thing"

    print (f"Your character is {hero}")
    print (f"Your opponent is {villain}")
    print ()
    
    ahs_Adrienne (Adrienne_user,Adrienne_comp)

def ahs_Adrienne (usr,cmp):

    # The Battle
    
    fn_user = usr
    fn_comp = cmp
    
    if usr == "a" and cmp == "h" or usr == "h" and cmp == "a":
        print ("Aqua Man extinguishes Human Torch")
        print ("So Aqua Man wins")
    elif usr == "h" and cmp == "s" or usr == "s" and cmp =="h":
        print ("Human Torch burns the Swamp Thing")
        print ("So Human Torch wins")
    elif usr == "s" and cmp == "a" or usr == "a" and cmp =="s":
        print ("Swamp Thing drowns Aqua Man")
        print ("So Swamp Thing wins")

    else:
        print ("The battle is a draw")
    print ()

main()
