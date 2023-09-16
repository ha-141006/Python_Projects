#code to reverse the string

# method 1

s=input('enter string: ')
r=''
for c in s:
 r=c+r
print(r)

#-----------------------------------#

# Method 2
print(''.join(reversed(s)))

#-----------------------------------#

# Method 3
print(s[::-1])