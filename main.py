#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

with open("nato_phonetic_alphabet.csv") as file:
    list = file.readlines()
    dictionary = {name[0]:name.split(",")[1][:-1] for name in list if name[0] != "l"}

word = input("Input a word: ")

try:
    result = [dictionary[letter.title()] for letter in word]
except KeyError:
    print("Sorry, only letters from alphabet please.")
else:
    print(result)

