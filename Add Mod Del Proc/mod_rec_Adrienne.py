# File: mod_rec_Adrienne.py
# Project: CSIS 2101 Assignment 11
# Author: Adrienne Pallett
# History: Version 11.1 November 20 2022

# Modify a Record

import os

def main():

    # Modify the Record
    try:
        in_file = open("grades.txt","r")
    except FileNotFoundError:
        print("The file you are trying to open hasnt been created yet.")
        
    temp_file = open("temp.txt","w")

    line = in_file.readline()

    student = str(input("Enter the first and last name of the student: "))
    old_grade = str(input("Enter the old grade of the student: "))
    new_grade = str(input("Enter the new grade: "))

    search = (f"{student} {old_grade}")

    found = False

    while line != "":
        line = line.strip("\n")

        if line == search:
            line = (f"{student} {new_grade}")
            
            found = True
        
        temp_file.write(line + "\n")

        line = in_file.readline()
    
    if found == True:
        in_file.close()
        temp_file.close()

        os.remove("grades.txt")
        os.rename("temp.txt","grades.txt")
    else:
        print(f"{student} not found.")
        
    in_file.close()

    # New Average
    in_file = open("grades.txt","r")

    line = in_file.readline()

    grades = 0
    counter = 0
    
    while line != "":
        line = line.strip("\n")
        data = line.split()
        
        counter += 1
        grades += int(data[-1])

        line = in_file.readline()

    if counter == 0:
        print("The file doesn't contain any grades, average cant be calculated")
    else:
        average = grades/counter

        print (f"The new average grade of {counter} students is {average:.1f}")

    in_file.close()

if __name__ == "__main__":
    main()
