# These function is an alternate way to find the area using semi-perimeter
import math

def main():

    print("I can find the area of a triangle using 'semi-perimeter'")

    triangle_area_adrienne()

def triangle_area_adrienne ():
    a,b,c = eval(input("Enter Sides separated by comma: "))

    is_valid_adrienne (a,b,c)
    calc_Area_adrienne (a,b,c)

    is_true = is_valid_adrienne (a,b,c)
    area = calc_Area_adrienne (a,b,c)

    if is_true == True: # Try again using a while loop
        print(f"Area of the triangle with sides {a}, {b} and {c} is \
{area:.03f} square inches")
    else:
        print("Invalid Input. Sum of any two sides has to be greater \
than the third side.")
        triangle_area_adrienne () #Causes recursive errors DONT DO IT. Same as calling main()

def is_valid_adrienne (a,b,c):
    if a + b > c and b + c > a and c + a > b: # should be (a+b)>c
        return True
    else:
        return False

def calc_Area_adrienne (a,b,c):
    s = (a+b+c)/2
    x = s*(s-a)*(s-b)*(s-c)

    if x < 0:
        return False

    area = math.sqrt(x)
    return area # because print out is in main() thats why it couldnt find area variable

main()
