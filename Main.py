"""Imports"""
import os
import random
"""System variables"""
normal_letters = {}
cripted_letters = {}
cripted_letters_MainKey = {}
cripted_letters_IddenKey = {}
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
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

#FOR CONVERT NUMBER
def convert(number=int, type=str):
    if type == "negative":
        return -number
    elif type == "positive":
        return +number
    else:
        print(f"{type} not found in function!")
#FOR SHOW THE MENU
def show_menu(): #I know there is a more efficient way to do that but this is the most readable and it's easier to modify it
    print("Type 1 for cript a message")
    print("Type 2 for decript a message (if you know the key)")
    print("Type 3 for the safe mode cript (you won't know the key)")
    print("Type 4 for decriptate and break the key")

#FOR CRIPTATE TEXT
def cript(text=str, decifration_key=int):
    for letter in alphabet:
        index = alphabet.index(letter)
        if (index + decifration_key) >= 26:
            index = (index + decifration_key) - 26
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
            index = (index - decifration_key) + 26
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
    attempt = 0
    while attempt <= 27:
        for letter in alphabet:
            index = alphabet.index(letter)
            if (index - decifration_key) <= -1:
                index = (index - decifration_key) + 26
            else:
                index = (alphabet.index(letter)) - decifration_key
            normal_letters.update({letter: index})
        result = ""
        for i in text:
            if i in alphabet:
                index_letter = normal_letters[i]
                normal_letter = alphabet[index_letter]
                result = result + normal_letter
        print(f"Attempt: {result}")
        print(f"Decifration key: {decifration_key}")
        separator()
        decifration_key += 1
        attempt += 1
    
#FOR A SAFEST CRIPT METHOD (even you don't know the key))
def SafeCript(text=str):
    #first encryption
    Maindecifration_key = random.choice(numbers)
    print("[Creating a random and safe key]...")
    for letter in alphabet:
        index = alphabet.index(letter)
        if (index + Maindecifration_key) >= 26:
            index = (index + Maindecifration_key) - 26
        else:
            index = (alphabet.index(letter)) + Maindecifration_key
        cripted_letters_MainKey.update({letter: (index)})
    MainResult = ""
    for i in text:
        if i in alphabet:
            index_letter = cripted_letters_MainKey[i]
            cripted_letter = alphabet[index_letter]
            MainResult = MainResult + cripted_letter
    #second encryption
    Hiddendecifration_key = random.choice(numbers)
    while Hiddendecifration_key == Maindecifration_key:
        Hiddendecifration_key = random.choice(numbers)
    for letter in alphabet:
        index = alphabet.index(letter)
        if (index + Hiddendecifration_key) >= 26:
            index = (index + Hiddendecifration_key) - 26
        else:
            index = (alphabet.index(letter)) + Hiddendecifration_key
        cripted_letters_IddenKey.update({letter: (index)})
    HiddenResult = ""
    for i in text:
        if i in alphabet:
            index_letter = cripted_letters_IddenKey[i]
            cripted_letter = alphabet[index_letter]
            HiddenResult = HiddenResult + cripted_letter
    lengthMain = len(MainResult) // 2
    lengthHidden = (len(HiddenResult) // 2)
    lengthHidden = -abs(lengthHidden)
    FinalResult = MainResult[:lengthMain] + HiddenResult[lengthHidden:]
    print(FinalResult)
    
"""Script"""
print("---Welcome to the Cripting Message System---")
while True:
    show_menu()
    action = input("Type a number: ")
    if action == "1":
        text1 = input("Type the text that you want to cript: ").lower()
        key = int(input("Type the decifration key for the cript (must be between 1 and 26): "))
        if key <= 26:
            text2 = cript(text1, key)
            print(f"Normal text: {text1}\nCripted text: {text2}")
        else:
            print("Key too big")
    elif action == "2":
        text1 = input("Type the text you want to decript: ").lower()
        key = int(input("Type the decifration key for the cript (must be between 1 and 26): "))
        if key <= 26:
            text2 = decript(text1, key)
            print(f"Cripted text: {text1}\nNormal text: {text2}")
        else:
            print("Key too big")
    elif action == "3":
        text = input("Type here the text to safe cript: ")
        SafeCript(text)
    elif action == "4":
        text = input("Type the take that you want decript (even without key): ")
        brutalForce(text)
    else:
        print("Invalid action!")