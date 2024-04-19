# File: app_rec_Adrienne.py
# Project: CSIS 2101 Assignment 11
# Author: Adrienne Pallett
# History: Version 11.1 November 20 2022

# Append a Record

def main():

    # Append Record
    in_file_r = open("grades.txt","r")
    
    in_file_a = open("grades.txt","a")

    line = in_file_r.readline()
    
    new_name = "Adrienne Pallett"
    new_grade = "89"
    
    found = False
    
    while line != "":
        line = line.strip("\n")

        if line == new_name:
            found = True
        
        line = in_file_r.readline()

    if found == False:
        in_file_a.write(f"{new_name} {new_grade}\n")     
    else:
        print("This student already exists")
             
    in_file_a.close()

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
