#Strings
# Take in a string, ask user to identify what should be replaced and with what. Finds the last of a 2+ instance of the string and replaces it.

def main():
    word = str(input("Enter your word: "))
    sub_str = str(input("What letter(s) should be replaced?: "))
    rep_str = str(input("What do you want to replace the last letter with?: "))
    

    # Q1 - Output

    aTReplace(word,sub_str,rep_str)
    
    result = aTReplace(word,sub_str,rep_str)
    
    if result in aTReplace(word,sub_str,rep_str):
        print("Your result is:",result)
    
    
def aTReplace(word,sub_str,rep_str):

    ##### New Version of Code ###

    # Finds
    index = word.find(sub_str)

    # If the string is not found at all
    if(index == -1 ):
        print("Your word doesnt contain the substring.")

    else:
        old_str = word[ :index+len(sub_str)]
        new_str = word[index+len(sub_str): ]
        index2 = new_str.find(sub_str)

        # If the string only contains 1 instance
        if index2 == -1:
            print("Your word only contains 1 instance. Nothing is changed.")

        else:
            new_index = len(old_str) + index2

        new_str = new_str.replace(sub_str,"&")
        
        count = 0
        for i in new_str:
            if i == "&":
                count += 1
            else:
                pass

        if count == 1:
            new_str = new_str.replace("&",rep_str)
            result = old_str + new_str
            return result

        else:

            if new_str.endswith("&") == True:
                new_str = new_str.rstrip("&")
                new_str = new_str + rep_str
                new_str = new_str.replace("&",sub_str)
                result = old_str + new_str
                return result

            else:
                new_str_r = new_str[::-1]
                final_index = new_str_r.find("&")
                new_str_r = new_str_r[:final_index] + rep_str + new_str_r[final_index+1:]           
                new_str = new_str_r[::-1]
                new_str = new_str.replace("&",sub_str)
                result = old_str + new_str
                
                return result
main()