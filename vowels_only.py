# given text as a string, print only the vowels in the string
# get user input as a string // lowercase the input
inp = input("Give me some text! ").lower()
vowels = "aeiouy"
# iterates through each letter in input
for letter in inp:
# checks if each letter in input is in vowels
    if letter in vowels:
# prints letter only if it is a vowel
        print(letter)