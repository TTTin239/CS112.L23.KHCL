import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
gt =(d*a - c*b)//(c-d)
dem=0
while (a*d!=b*c):
  a = a + 1
  b = b + 1
  ucln = math.gcd(a,b)
  a = a//ucln
  b = b//ucln
  dem+=1
  if dem > gt:
    break
if dem > gt: 
  print(0)
else:
  print(dem)