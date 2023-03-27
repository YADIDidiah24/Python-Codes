import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*-_.'/")

def generatePassword():

    len_password = int(input("Enter the length of password: "))

    random.shuffle(characters)

    password= []
    for i in range(len_password):
        password.append(random.choice(characters))

    random.shuffle(characters)

    password = "".join(password)

    return password

option = input("Do you want ot generate a password? (Yes/No): ")

if option.lower() == "yes" or option.lower() == "y":
    print(f"your generated password is : {generatePassword()}")
else:
    print("program Ended......")




