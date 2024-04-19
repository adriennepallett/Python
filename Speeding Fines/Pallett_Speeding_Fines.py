# File: Pallett_Speeding_Fines.py
# Project: CSIS 2101 Assignment 3
# Author: Adrienne Pallett
# History: Version 3.1 September 9, 2022

# Nested Function

def Pallett_Speeding_Fines():

    # Input - User Enters Ticket Details
    
    # Variables
    
    speedLimit_zone_Adrienne = float(input("Speed Limit: "))
    speed_veh_Adrienne = float(input("Vehicle Speed: "))
        # int(input())
    miles_over = speed_veh_Adrienne - speedLimit_zone_Adrienne

    driv_teen = input("Teen Driver: ")
    #
    fine_1 = 39.50
    fine_2 = 89.00
    fine_3 = 109.50
    fine_4 = 149.99
    fine_5 = 0.00

    fine_1t = 3 * fine_1
    fine_2t = 3 * fine_2
    fine_3t = 3 * fine_3
    fine_4t = 3 * fine_4
    fine_5t = 3 * fine_5
    # Shouldnt be calculated
    tfc = "Total Fine Calculated : $"

    # Loop
    if miles_over < 5 and driv_teen == 'n' or driv_teen == 'no':
        print(f"{tfc} {fine_1:.02f}")
        print("You can do better as a driver!")
    elif miles_over < 15 and driv_teen == 'n' or driv_teen == 'no':
        print(f"{tfc} {fine_2:.02f}")
        print("Please reduce your speed!")
    elif miles_over < 25 and driv_teen == 'n' or driv_teen == 'no':
        print(f"{tfc} {fine_3:.02f}")
        print("Be careful, you are driving recklessly!")
    elif miles_over < 35 and driv_teen == 'n' or driv_teen == 'no':
        print(f"{tfc} {fine_4:.02f}")
        print("You are over-speeding!")
    else:
        if miles_over >= 35 and driv_teen == 'n' or driv_teen == 'no':
            print(f"{tfc} {fine_5:.02f}")
            print ("Court is mandatory. Your fine will be decided in court")
        else:
            print("nothing")
        # Above statement is completely wrong
    # all operators should be >= or <=
    # first condition < > = last condition < >
    
    #else:
    if miles_over < 5 and driv_teen == 't' or driv_teen == 'teen':
        print(f"{tfc} {fine_1t:.02f}")
        print("You can do better as a driver!")
    elif miles_over < 15 and driv_teen == 't' or driv_teen == 'teen':
        print(f"{tfc} {fine_2t:.02f}")
        print("Please reduce your speed!")
    elif miles_over < 25 and driv_teen == 't' or driv_teen == 'teen':
        print(f"{tfc} {fine_3t:.02f}")
        print("Be careful, you are driving recklessly!")
    elif miles_over < 35 and driv_teen == 't' or driv_teen == 'teen':
        print(f"{tfc} {fine_4t:.02f}")
        print("You are over-speeding!")
    elif miles_over >= 35 and driv_teen == 't' or driv_teen == 'teen':
        print(f"{tfc} {fine_5t:.02f}")
        print ("Court is mandatory. Your fine will be decided in court")
    # should only be 3 condition statements. too excessive.
    else:
        if driv_teen != 't' or 'n' or 'no' or 'teen':
            print ("Invalid Entry. Please Enter T or N.")
                
    # Output - User Sees Ticket Price and Speeding Message


Pallett_Speeding_Fines()
