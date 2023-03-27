[a,k,b,m,n] =list(map(int,input().split()))

lmao=int(n//(a+b-a/k-b/m))
for i in range(lmao-100,lmao+100):
  vcc=i*(a+b)-a*(i//k)-b*(i//m)
  if (vcc>=n):
    print(i)
    break