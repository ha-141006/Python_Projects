#convert a list of characyers to a string

# method 1

l = input('Enter your list: ').split()
print(''.join(l))
#-----------------------------------------#

# Method 2
s=''
for c in l:
 s=s+c
print(s)