n=input()
def xuli(n):
  s=int(n)
  ds=list(n)
  mod=s%3
  b={ 1:[7,4,1],2:[8,5,2],3:[9,6,3]}
  c=0
  h=1
  while h!=0:
    for i in range (len(ds)):
      ds[i] = int(ds[i])
      for j in b[3-mod]:
        if ds[i]+j<10:
          ds[i]=ds[i]+j
          h=0
          c=1
          break
      if h==0:
        break
    h=0
  if c==0:
    if mod!=0:
            ds[-1] = int(ds[-1])-mod
    else:
            ds[-1] = int(ds[-1])-3

  return ''.join([str(x) for x in ds])
print(xuli(n))