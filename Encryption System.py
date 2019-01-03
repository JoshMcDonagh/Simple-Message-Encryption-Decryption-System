# --- MODULE IMPORTS ---
from decimal import *
    


# --- GLOBAL VARIABLE DECLARATIONS ---
SET_PREFIX = "21gh4"



# --- FUNCTION DEFINITIONS ---

# Function takes plain code string and returns encrypted cypher code
def Encrypt(plain, seed):
    cypher = ""

    # Encrypts each char of the plain-text
    for char in plain:
        cypher += str((ord(char) + 10) ** seed)
        cypher += ";"
        
    cypher += "!"
    
    return cypher


# Function takes cypher code string and returns decrypted plain code
def Decrypt(cypher, seed):
    plain = ""
    char_code = 0

    # Decrypts each char of the cypher-text
    for char in cypher:
        if char != ";" and char != "!":
            char_code *= 10
            char_code += int(char)
            
        elif char == ";":
            plain += chr(int(Decimal(char_code) ** Decimal(1 / seed)) - 9)
            char_code = 0
    
    return plain


# Function takes a string and turns it into a password seed
def GetSeed(password):
    seed = 0

    # Sums the ASCII codes of each password char
    for char in password:
        seed += int(ord(char))

    return seed


# Function writes to a file
def WriteToFile():
    global SET_PREFIX
    file = 0
    seed = 0
    password = ""
    message = ""

    # Makes sure valid file name input
    while True:
        file_name = input("File name: ")
        file_name += ".txt"

        print("")

        try:
            file = open(file_name, "w")
            break
        
        except:
            print("File name given was invalid.")

    password = input("New password: ")
    print("")

    seed = GetSeed(password)

    message = input("Text to enter:\n")
    print("")

    message = SET_PREFIX + message

    file.write(Encrypt(message, seed))
    file.close()

    print("Success.\n")


# Function reads from a file
def ReadFromFile():
    global SET_PREFIX
    file = 0
    message = ""
    cypher = ""

    # Makes sure valid file name input
    while True:
        file_name = input("File name: ")
        file_name += ".txt"

        print("")

        try:
            file = open(file_name, "r")
            break

        except:
            print("File name given was invalid.")

    cypher = file.read()
    file.close()

    # Makes sure correct password is input
    while True:
        password = input("Password: ")
        print("")

        # Checks to make sure characters have actually been input
        if password != "":
            message = Decrypt(cypher, GetSeed(password))
        else:
            print("Password entered is incorrect.")
            continue
        
        # Checks to make sure the prefix decoded is correct
        if message[0:5] == SET_PREFIX:
            message = message[5:]
            break
        else:
            print("Password entered is incorrect.")

    print("Message:\n" + message + "\n")



# --- MAIN ---

cmd_list = ["WRITE", "READ", "HELP"]

while True:
    user_cmd = input("Enter a command: (type 'HELP' for a list of commands) ").upper()
    print("")

    # Checks if the user has chosen to write to a file
    if user_cmd == cmd_list[0]:
        WriteToFile()

    # Checks if the user has chosen to read from a file
    elif user_cmd == cmd_list[1]:
        ReadFromFile()

    # Checks if the user has chosen to get help
    elif user_cmd == cmd_list[2]:
        for cmd in cmd_list:
            print(cmd)
        print("")

    # Determines finally what do in the case of an invalid input
    else:
        print(user_cmd + " is an invalid command.\n")
    
