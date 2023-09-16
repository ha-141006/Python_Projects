#convert a string to s square matrix grid of characters

s=input('square matrix convertor: ')

import math
n=math.ceil(math.sqrt(len(s)))

for i in range(n):
 print(s[i*n:(i+1)*n].ljust(n,'*'))