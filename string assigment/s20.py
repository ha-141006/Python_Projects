'''
# Accept a String from the user and determine if it is Heterogram
# Heterogram is a word, phrase, or sentence in which no letter of the alphabet occurs more than once.
'''

x = input('\nEnter String  : ')
print(len(set(x))==len(x))

