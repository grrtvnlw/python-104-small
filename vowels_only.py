# given text as a string, print the text in leetspeak
# get user input as a string // lowercase the input
inp = input("Give me some text! ").lower()
vowels = "aeiouy"

for letter_inp in inp:
    for letter_vowels in vowels:
        if letter_inp == letter_vowels:
            print(letter_vowels)