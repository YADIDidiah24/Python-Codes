import string

LowerCaseLetter = string.ascii_lowercase # a,b,c,d,e,f,....z

def NFA():
    states = {"q0":"","q1":"","q2":"","q3":True} # states

    word = input("Enter the word: ") # input

    for char in word[:-3]: # to check every char excluding the last 3
        if char not in LowerCaseLetter: # if character is not lowercase
            print("INVALID, REJECTED ") # then reject
            return


    if word[-3] == "m": # if the third last word is "m"
        states["q0"] = "q1" # then q0-> q1

    if word[-2] == "a": # if the second last word is "a"
        states["q1"] = "q2" # then q1-> q2

    if word[-1] == "n": # if the last word is "n"
        states["q2"] = "q3" # then q2-> q3
        states["q3"] = "q3" # q3 is the final state


    if states["q0"] == "q1" and states["q1"] == "q2" and states["q2"] == "q3": # to check if all conditions meet.
        print("INPUT ACCEPTED!!!") # input string is accepted
    else:
        print("rejected...")


NFA() # calling the function




    

