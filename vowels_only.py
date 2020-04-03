# given text as a string, print the text in leetspeak
# get user input as a string // lowercase the input
inp = input("Give me some text! ").lower()
vowels = "aeiouy"
# checks each letter in input
for letter_inp in inp:
# checks each letter in vowels
    for letter_vowels in vowels:
# compares letter in vowels with letter in input
        if letter_inp == letter_vowels:
            print(letter_vowels)