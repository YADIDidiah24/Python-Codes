import string

letters = string.ascii_letters # letters (a-z and A-Z) lowercase and uppercase
digits = string.digits # numbers from (0-9)

states = {"q0":"","q1":"","q2":""}  # dictionary for states
# q0 = initial state
# q1 = final state
# q2 = dead state
word = input("Enter the word: ") # input form user


if word[0] in letters: # to check if first character is a letter
    states["q0"] = "q1" # then q0 -> q1
    states["q1"] = "q1" # q1 -> q1
else: #else
    states["q0"] = "q2" # q0 -> q2 (dead state)
    states["q2"] ="q2"  # q2 -> q2 

if word.isalnum(): # returns True if all characters in the string are alphanumeric
    states["q1"] ="q1" # q1 -> q1

else:
    states["q1"] ="q2" # q1 -> q2 (dead state)
    states["q2"] ="q2" # q2 -> q2


if states["q0"] == "q2" or states["q1"] == "q2" or states["q2"] == "q2": # checking states q0 and q1

    print("INPUT REJECTED")
    print()
    print(f"The word {word} is not an identifier")
else:

    print("INPUT ACCEPTED!")
    print()
    print(f"The word {word} is an IDENTIFIER!")
    

