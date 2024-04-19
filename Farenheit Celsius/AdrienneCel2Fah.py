# File: AdrienneCel2Fah.py
# Project: CSIS 2101 Celsius to Farenheit Conversion
# Author: Adrienne Pallett
# History: Version 2.1 September 4, 2022

# This program converts a user input of Celsius measure and converts to
#   Farenheit
# Input collects temperature from user in Celsius
# Output displays temperature given in celsius to farenheit

# Celsius to Farenheit Conversion Equation
# Cel * 9/5 + 32

def main ():
    print ("I will help you convert temperatures from Celsius to Farenheit")
    AdrienneCel = float(input("Enter the temperature in Celsius:"))

    PallettCel = AdrienneCel * 9/5 + 32

    print(f"The temperature {AdrienneCel} degrees Celsius is {PallettCel:.3f} \
degrees Farenheit")

main()
