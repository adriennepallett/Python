# Function with 1 parameter for rows of ampersands to display according to input
#   with a nested loop

def Assignment5_Part2() :
    def Adrienne_ampersand_sign():
        n= int(input("Enter prints: "))
        print("& " * n,end=" ")
        print()

        for p in range (n,0,-1):
            for q in range (p - 1):
                print("&",end=" ")
            print()
  
    Adrienne_ampersand_sign()

Assignment5_Part2()