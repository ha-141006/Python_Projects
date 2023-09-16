# Check if a string(s2) can be constructed out of another string(s1)

s1=input('\nstring_1: ')
s2=input('string_2: ')

def contains(s1,s2):
 for c in s2:
  i=s1.find(c)
  if i==-1: return False
  s1=s1[:i]+s1[i+1:]
 return True

print(contains(s1,s2))
