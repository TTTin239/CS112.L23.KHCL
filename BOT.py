n = int(input())
a = list(map(int, input().split()))
maxsum = 0;
sum = 0;
i=0
vtdkq=0
vyckq=0
vtdtam=0
for i in range(n):
  sum += a[i];
  if (sum < 0): 
    sum = 0
    vtdtam=i+1
  if (sum>maxsum):
    vtckq=i
    vtdkq=vtdtam
    maxsum=sum

print(vtdkq+1,vtckq+1,maxsum)