# File: Menu_Adrienne.py
# Project: CSIS 2101 Assignment 7 - Menu
# Author: Adrienne Pallett
# History: Version 7.1 October 19, 2022

# Menu Program to Find Volumes of a user entered desire of 3D Shapes
# This is the main root program that uses a program of functions to determine
#   the appropriate output to display

import Volumes_Adrienne

# Program Introduction
print("This program will calculate various volumes of 3D shapes")

# Program
def main ():

    # Menu
    menu_Adrienne()

    # User's Choice
    option = int(input("\nEnter your choice: "))

    # Input Validation
    is_valid_input = valid_input(option)
    
    # If User Enters an Invalid Input
    while is_valid_input == False or option > 5:
        print ("You did not choose a valid selection. Try Again")
        option = int(input("\nEnter your choice: "))
        
    # Volume Outputs
    while is_valid_input == True and option < 5:
    #While option !=5:
        # if option<1 or option >5:
            # option = int(input(" Invalid input. Enter your choice 1-5: "))
        
        if option == 1:
            print ("\nVolume of a Sphere")
            r = eval(input("Enter Radius of the sphere: "))
            vol_sph = Volumes_Adrienne.sphereVolumeAdrienne(r)
            print (f"Volume of the sphere with radius {r} in. is {vol_sph:.2f} \
cubic inches \n")
            
        elif option == 2:
            print ("\nVolume of a Cylinder")
            r = eval(input("Enter Radius of the cylinder: "))
            h = eval(input("Enter Height of the cylinder: "))
            vol_cyl = Volumes_Adrienne.cylVolumeAdrienne(r,h)
            print (f"Volume of the cylinder with a radius {r} in. and height \
{h} in. is {vol_cyl:.2f} cubic inches \n")
            
        elif option == 3:
            print ("\nVolume of a cone")
            r = eval(input("Enter Radius of the cone: "))
            h = eval(input("Enter Height of the cone: "))
            vol_cone = Volumes_Adrienne.coneVolumeAdrienne(r,h)
            print (f"Volume of this cone with radius {r} in. and height \
{h} in. is {vol_cone:.2f} cubic inches \n")
            
        elif option == 4:
            print ("\nVolume of a Cube")
            s = eval(input("Enter Sides of the cube: "))
            # while not(valid_input(s)):
            #   s = eval(input("Invalid entry please reenter: "))
            vol_cube = Volumes_Adrienne.cubeVolumeAdrienne(s)
                #Not necessary
            print (f"Volume of the cube with sides {s} in. is {vol_cube:.2f} \
cubic inches \n")
            # print (f"Volume of the cube with sides {s} in. is
#{Volumes_Adrienne.cubeVolumeAdrienne(s):.2f} cubic inches \n")

        menu_Adrienne ()
        option = int(input("\nEnter your choice: "))
        
    while is_valid_input == True and option != 5:
        option = int(input("\nEnter your choice: "))
        
    if option == 5:
        print ("Good-Bye \n")


# Menu
def menu_Adrienne():
    
    print ("\n_______Menu_______")
    print ("1. Volume of a Sphere")
    print ("2. Volume of a Cylinder")
    print ("3. Volume of a Cone")
    print ("4. Volume of a Cube")
    print ("5. Exit")


# Input Validation Function
def valid_input(option): # valid_input(x):
    
    if option > 0:  #if x > 0:
        return True
    else:
        return False
    
main()
