# Code to rotate the string n times anti-clockwise

s=input('\nEnter String Clockwise Rotation : ')
n=int(input('No. of Rotations Anti-clockwise : '))

n=n%len(s)
s=s[n:]+s[:n]
print(s)