#convert a string so that it holds only distinct characters

# Method 1
s=input('convert to distinct characters: ')
n=set(s)
print(n)
#-------------------------------------------#

# Method 2

x={c for c in s}
print(x)