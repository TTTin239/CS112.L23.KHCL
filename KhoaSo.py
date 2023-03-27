st=input().strip()
a=[0,0,0,0,0,0,0,0,0,0]
s=0
def delnummod(a,mod,dmod):
  for i in mod:
      if a[i]>0:
        a[i]-=1
        break
  else:
    d=0
    for i in dmod:
      if a[i]>=2:
        a[i]-=2
        d+=2
      elif a[i]==1:
        a[i]-=1
        d+=1
      if d==2:
        break
for i,j in enumerate(st):
  t=int(j)
  s+=t
  a[t]+=1
mod=s%3
sur1=[1,4,7]
sur2=[2,5,8]
if mod==1:
  delnummod(a,sur1,sur2)
elif mod==2:
  delnummod(a,sur2,sur1)
result=''
for i in range(9,-1,-1):
    result+=str(i) * a[i]
print(result)