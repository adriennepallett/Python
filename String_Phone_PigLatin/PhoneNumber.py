#Phone Number conversion
# takes in a word phone number and returns the numerical equivelent

def main():
    number = str(input("Enter a 7 or 10 digit alphanumeric phone number to \
    convert: "))

    # Q2 - Output
    print("The digit phone number is:",aTNumberConverter(number))

def aTNumberConverter(number):

    # Letter String
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Accounting for Lowercase
    numberLower = " "
    
    for i in number:
        if i.isdigit():
            numberLower += i
        elif i == "-" or i == " ":
            numberLower += i
        elif i.islower():
            numberLower += i.upper()
        else:
            numberLower += i
    
        number = numberLower
    
    
    # For Loop to Reassign Letters to Numbers
    for i in number:
        if i.isdigit():
            pass          
        else:
            if i in letters[0:3]:
                number = number.replace(i,"4")
            elif i in letters[3:6]:
                number = number.replace(i,"5")
            elif i in letters[6:9]:
                number = number.replace(i,"6")
            elif i in letters[9:12]:
                number = number.replace(i,"7")
            elif i in letters[12:15]:
                number = number.replace(i,"8")
            elif i in letters[15:19]:
                number = number.replace(i,"9")
            elif i in letters[19:22]:
                number = number.replace(i,"3")
            else:
                if i in letters[22:26]:
                    number = number.replace(i,"2")
    return number
main()