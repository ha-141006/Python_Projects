# Remove all characters other than alphabets in the string

s=input('\nEnter string : ')
print(''.join(filter(str.isalpha, s)))