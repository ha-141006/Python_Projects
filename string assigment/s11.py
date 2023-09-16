# code to reverse the words in the string

s=input('\nReverse String : ')
print(' '.join(map(lambda x : x[::-1],s.split(' '))))