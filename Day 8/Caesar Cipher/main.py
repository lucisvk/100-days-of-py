import os 
import random 
import math 




print("""\n\n\n ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88     """)




  
def encrypt(message, shift):
    result = []

    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)

    print(result)

def decrypt(message, shift):
    return encrypt(message, -shift)

user_option = input("\n\nType encode to encrypt a message, or type decode to decrypt a message: ")
if user_option == 'encode':
    userin = input("Please enter your message: ")
    shiftnum = int(input("Please type the shift number: "))
  
    encrypt(userin, shiftnum)

elif user_option == 'decode': 
    userin = input("Please enter your message: ")
    shiftnum = int(input("Please type the shift number: ")) 
    decrypt(userin, shiftnum)
else: 
    print("Invalid Option")




