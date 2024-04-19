# File: Assgn9Pallett.py
# Project: CSIS 2101 Assignment 9
# Author: Adrienne Pallett
# History: Version 9.3 November 8, 2022

# Pig Latin

def main():
    
    sent = str(input("Enter your sentence to convert to pig latin: "))

    print("Your pig latin is:",aTPigLatin(sent))
    
def aTPigLatin(sent):
    
    startList = sent.split(" ")

    # Index the list
    index = len(startList)

    # Create empty list to append into
    wordList = []

    # For Loop to restructure the elements
    for i in startList:
        if len(i) == 1:
            wordList.append(i + "st ")
        else:
            endLetter = i[len(i)-1]
            i = i[:-1]
            i = endLetter+i
            wordList.append(i +"st ")

    pigLatin = " "
    for i in wordList:
        pigLatin += i
    
    return pigLatin
    

main()

