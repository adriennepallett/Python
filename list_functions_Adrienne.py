# File: list_functions_Adrienne.py
# Project: CSIS 2101 Assignment 8 List Functions
# Author: Adrienne Pallett
# History: Version 8.1 October 29, 2022


# Import Functions

import random


def Adrienne_list():

    '''
    should have asked user to enter number of values and values separated by
    ,
    '''
    # n = int(input"enter number of values:"))
    
    # User inputs list values
    userList = []
    # for value in range (n):
    #   num(int(input("please enter value" +str(value)+ number:"))
    #   userList.append(num)
    
    # Loop to append user entered numbers into the list - While
    listWhile = "y"

    ''' This while loop is not needed'''
    while listWhile == "y":
        n = int(input("Enter your value: "))
        userList.append(n)

        print ("Do you want to add more numbers?")
        listWhile = input("y for yes or n for no: ")
        print()

    print("Your List: ",userList)
    print()


    # Random List
    randomList = []

    for i in range(0,len(userList)):
        n = random.randint(10,99)
        randomList.append(n)
        
    print("A random list of numbers is: ",randomList)

    
    # Deep Copy of userList
    userList_copy = []
    for num in userList:
        userList_copy.append(num)
    # print("copies list:",userList_copy)


    # Sort Copied List
    userList_copy.sort()


    # Functions to be returned
    # print("range of the number list:",range_list_Adrienne(userList))
    range_list_Adrienne(userList)
    # print("mean of the list:",mean_list_adrienne(userList))
    mean_list_Adrienne(userList)
    # print("median of the list:",median_list_adrienne(userList_copy))
    median_list_Adrienne(userList_copy)
    # print("intersection of the list:",intersection_list_adrienne(userList_copy,randomList))
    intersection_list_Adrienne(userList,randomList)

    union_list_Adrienne(userList,randomList)


    # Prints using returned values from various list functions
    # Functions with first list


def range_list_Adrienne(userList):
    # Returns the range of the list given by the user - any digits
    # Max value - min value = range

    rangeList = max(userList)-min(userList)
    print("Range of the list is: ",rangeList)

    # if len(userList) > 0:
    #   return max(userList)-min(userList)
    # else:
    #   print("list is empty")
        
    
def mean_list_Adrienne(userList):
    # Returns the mean of the list
    # Use Sum function to calculate the the average

    sumList = sum(userList)
    meanList = sumList / len(userList)
    
    print("Mean of the list is: ",meanList)

    # if len(userList) > 0:
    #   return sum(UserList)/len(userList)
    # else:
    #   print("list is empty")    
    

def median_list_Adrienne(userList_copy):
    # Returns the median of the list
    # Copy userList using append function and send to main as an arguement

    # sort function
    # print("sorted list:",userList_copy)
    
    ln = len(userList_copy)

    # if ln_list > 0:
    if ln % 2 == 0:
        median_1 = userList_copy[ln//2]
        median_2 = userList_copy[ln//2-1]
        medianList = (median_1 + median_2)/2
        print(medianList)
    else:
        medianList = userList_copy[ln//2]
    # else:
    #   ("list is empty")
    
    print("Median of list is: ",medianList)
    print()

    

    print("--- Second Round - Using Your List & A Random List --- ")
    print()
    
    
def intersection_list_Adrienne(userList,randomList):
    # Returns a new list where the values of userList and random list that are
    #   in common is what is returned
    
    print("A random list of numbers is: ",randomList)
    
    intersectList = []

    print("Your list: ",userList)
    print()

    for i in userList:
        if i not in randomList:
            pass
        else:
            intersectList.append(i)
    
    print("Intersection of the list: ",intersectList)

    
def union_list_Adrienne(userList,randomList):
    # Returns a new list list with numbers in common for userList and random
    #   list - exclude matching values
    # Make sure that if a list contains multiple same values, those are returned

    unionList = []

    for i in userList:
        if i not in randomList:
            unionList.append(i)
        for j in randomList:
            if j not in unionList:
                unionList.append(j)

    unionList.sort()

    print("Union of the list: ",unionList)


Adrienne_list()
