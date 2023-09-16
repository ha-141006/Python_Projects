#code to print common chracters of two strings in sorted order

s = input('enter first string: ')
n = input('enter second string: ')

x = sorted(set(s) & set(n))
print(x)
