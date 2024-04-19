# File: AdrienneFah2Cel.py
# Project: CSIS 2101 Farenheit to Celsius Conversion
# Author: Adrienne Pallett
# History: Version 2.1 September 4, 2022

# This program converts a user input of Farenheit measure and converts to
#   Celsius
# Input collects temperature from user in farenheit
# Output displays temperature given in farenheit to celsius

# Farenheit to Celsius Conversion Equation
# (Fah - 32) * 5/9

def main ():
    print ("I will help you convert temperatures from Farenheit to Celsius")
    AdrienneFah = float(input("Enter the temperature in Farenheit:"))

    PallettFah = (AdrienneFah - 32) * 5/9

    print(f"The temperature {AdrienneFah} degrees Farenheit is {PallettFah:.3f}\
 degrees Celsius")

main()
