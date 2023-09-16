# code to extract n bits from the number

x=int(input('enter first number: '))
n=int(input('enter no. of times: '))
print(bin(x)[2:][n-3:])