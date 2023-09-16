'''
# Accept a string from the user and determine if it is an Isogram
# Isogram is A word or phrase in which each letter occurs the same number of times
'''

s = input('\nEnter String  : ')
print(len(s) == len(set(s.lower().replace(" ", ""))))

