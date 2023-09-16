'''
# Accept a string from the user and determine if it is a Pangram
# A Pangram is a sentence containing every letter of the alphabet.
'''

s=input('\nEnter string : ')
print(len(set(filter(str.isalpha,s)))==26)