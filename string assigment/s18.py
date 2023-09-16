'''
# Accept Two strings from the user and determine if it is a Anagrams
# A Pangram is a word, phrase, or name formed by rearranging the letters of another.
'''
# Method 1

x=input('\nEnter string_1  : ')
y=input('Enter string_2  : ')

d={chr(c):0 for c in range(128)}
for i in range(len(x)):
 d[x[i]]+=1
 d[y[i]]-=1


print(not any(d.values()))

#-----------------------------------#
# Method 2
print(sorted(x)==sorted(y))