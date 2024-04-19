# Question 3
# CSIS Old McDonald Remix

def Assignment5_Part3():
    def Adrienne_nursery_rhyme():

        nursery_rhyme("cow","moo")
        nursery_rhyme("duck","quack")
        nursery_rhyme("pig","oink")

    def nursery_rhyme(animal,sound):
        intro()
        infunction(animal)
        here_there(sound)
        everywhere(sound)
        intro()
        print()
    
    def intro():
        print("Old CSIS2101 had a function, 1-0-1-0-1")
    def infunction(animal):
        print(f"And in this function he has a {animal}, 1-0-1-0-1")
    def here_there(sound):
        print(f'Here a "{sound}" there a "{sound}"')
    def everywhere(sound):
        print(f'Everywhere a "{sound}-{sound}"')
    
    Adrienne_nursery_rhyme()

Assignment5_Part3()