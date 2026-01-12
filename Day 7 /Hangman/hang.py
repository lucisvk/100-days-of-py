import os 
import math 
import random 

words = ('ant baboon').split()

chosen_word = random.choice(words) 

print(
        
"""                                                                            
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
8b,dPPYba,   
88P'   `"8a  
88       88  
88       88  
88       88                """) 



print("\nHello and welcome to hangman")
print("Rules are simple guess all the letters to a random word and you win")
print("You have 6 chances to guess the right word each wrong guess will gain a limb.")
print("Get all limbs put on and you lose ready! lets go!") 

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("Your chosen word has",len(chosen_word), "Letters")

def create_spacers():
    spacerlist =["_"] * len(chosen_word)
    return spacerlist

def addletter(spacerlist,letter, index): 
  spacerlist[index] = letter
  return spacerlist


spacerlist = create_spacers()
print(spacerlist)



trycounter = 0 



while trycounter < 6:
    userin = input("Please guess a letter: ").lower().strip()

    if len(userin) != 1:
        print("Please enter exactly one letter.")
        continue

    found = False

    for index, char in enumerate(chosen_word):
        if userin == char:
            found = True
            addletter(spacerlist, userin, index)

    if found:
        print("Great job! You guessed the correct letter:", userin)
        print(hangman[trycounter])
    else:
        print("Sorry, that guess was wrong. A part has been added.")
        trycounter += 1
        print(hangman[trycounter])

    print("Current word:", " ".join(spacerlist))
    print("Guesses left", 6-trycounter)

    if "".join(spacerlist) == chosen_word: 
        print("Hey great job you guessed the word in",trycounter, " trys.")
        break


if (trycounter == 6): 
    print("Sorry it looks like your all out of guesses the correct word was", chosen_word)

