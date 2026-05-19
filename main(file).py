"""Neural connection"""


"""Imports"""
import time
import os
import random
"""System variables"""
normal_letters = {}
cripted_letters = {}
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
predefinite_decifrationKey = 3
ultra_safe_predefinite_decifrationKey = 12
"""Functions"""

#FOR SEPARATE TEXT
def separator(character="-"):
    try:
        lenght = os.get_terminal_size().columns
    except OSError:
        lenght = 80
    print(character * lenght)

#FOR CRIPTATE TEXT
def cript(text=str, decifration_key=int):
    for letter in alphabet:
        index = alphabet.index(letter)
        if (index + decifration_key) >= 26:
            index = (index + decifration_key) - 27
        else:
            index = (alphabet.index(letter)) + decifration_key
        cripted_letters.update({letter: (index)})
    result = ""
    for i in text:
        if i in alphabet:
            index_letter = cripted_letters[i]
            cripted_letter = alphabet[index_letter]
            result = result + cripted_letter

    return result

#FOR DECRIPTATE TEXT
def decript(text=str, decifration_key=int):
    for letter in alphabet:
        index = alphabet.index(letter)
        if (index - decifration_key) <= -1:
            index = (index - decifration_key) + 27
        else:
            index = (alphabet.index(letter)) - decifration_key
        normal_letters.update({letter: index})
    result = ""
    for i in text:
        if i in alphabet:
            index_letter = normal_letters[i]
            normal_letter = alphabet[index_letter]
            result = result + normal_letter

    return result

#FOR DECRIPTATE TEXT (try) EVEN WITHOUT KEY
def brutalForce(text):
    decifration_key = 1
    attemp = 0
    while attemp <= 27:
        for letter in alphabet:
            index = alphabet.index(letter)
            if (index - decifration_key) <= -1:
                index = (index - decifration_key) + 27
            else:
                index = (alphabet.index(letter)) - decifration_key
            normal_letters.update({letter: index})
        result = ""
        for i in text:
            if i in alphabet:
                index_letter = normal_letters[i]
                normal_letter = alphabet[index_letter]
                result = result + normal_letter
        print(f"Attemp: {result}")
        print(f"Decifration key: {decifration_key}")
        separator()
        decifration_key += 1
        attemp += 1
    
#FOR A SAFEST CRIPT METHOD (even you don't know the key))
def SafeCript(text=str):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    #prima cifrazione
    Maindecifration_key = random.choice(numbers)
    print("[Creating a random and safe key]...")
    for letter in alphabet:
        index = alphabet.index(letter)
        if (index + Maindecifration_key) >= 26:
            index = (index + Maindecifration_key) - 27
        else:
            index = (alphabet.index(letter)) + Maindecifration_key
        cripted_letters.update({letter: (index)})
    result = ""
    for i in text:
        if i in alphabet:
            index_letter = cripted_letters[i]
            cripted_letter = alphabet[index_letter]
            result = result + cripted_letter
    #second criptation
    Iddendecifration_key = random.choice(numbers)
    while Iddendecifration_key == Maindecifration_key:
        Iddendecifration_key = random.choice(numbers)
    for letter in alphabet:
        index = alphabet.index(letter)
        if (index + Iddendecifration_key) >= 26:
            index = (index + Iddendecifration_key) - 27
        else:
            index = (alphabet.index(letter)) + Iddendecifration_key
        cripted_letters.update({letter: (index)})
    Second_result = ""
    for i in text:
        if i in alphabet:
            index_letter = cripted_letters[i]
            cripted_letter = alphabet[index_letter]
            Second_result = Second_result + cripted_letter
    FinalResult = (result[:int((len(result)/2))]+ Second_result[:-int((len(Second_result)/2))])#TO DO: fix this
    print(f"Final result: {FinalResult}")

    print(f"Normal key: '{result}' created with a {Maindecifration_key} key")
    print(f"Idden key: '{Second_result}' created with a {Iddendecifration_key} key")
    
"""Script"""
print("---Welcome to the Cripting Message System---")
while True:
    action = input("Type 1 for cript a message, type 2 for decript it (if you know the key), type 3 for break the key: ")
    if action == "1":
        text1 = input("Type the text that you want to cript: ").lower()
        key = int(input("Type the decifration key for the cript (must be betwin 1 and 26): "))
        if key <= 26:
            text2 = cript(text1, key)
            print(f"Normal text: {text1}\nCripted text: {text2}")
        else:
            print("Key too big")
    elif action == "2":
        text1 = input("Type the text you want to decript: ").lower()
        key = int(input("Type the decifration key for the cript (must be betwin 1 and 26): "))
        if key <= 26:
            text2 = decript(text1, key)
            print(f"Cripted text: {text1}\nNormal text: {text2}")
        else:
            print("Key too big")
    elif action == "3":
        text = input("Type the take that you want decript (even without key): ")
        brutalForce(text)
    else:
        print("Invalid action!")
        SafeCript(action)