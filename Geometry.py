# Bài tập về nhà của nhóm 9
import math
n = int(input())
x=[]
y=[]
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
K=[]
for i in range(n):
   x.append(list(map(int, input().split())))
min = math.dist(x[0],x[1])
for i in range(n):
    for j in range(i+2,n):
        y.append(math.dist(x[0], x[j]))
        if(min>y[i]):
            min = y[i]
    for a in range (i+2,n):
        A.append(math.dist(x[1], x[a]))
        if(min>A[i]):
            min = A[i]
    for b in range(i+3, n):
        B.append(math.dist(x[2], x[b]))
        if(min>B[i]):
            min=B[i]
    for c in range(i+4,n):
        C.append(math.dist(x[3], x[c]))
        if(min>C[i]):
            min=C[i]
    for d in range(i+5,n):
        D.append(math.dist(x[4], x[d]))
        if(min>D[i]):
            min = D[i]
    for e in range(i+6, n):
        E.append(math.dist(x[5], x[e]))
        if(min>E[i]):
            min=E[i]
    for f in range(i+7,n):
        F.append(math.dist(x[6], x[f]))
        if(min>F[i]):
            min=F[i]
    for g in range(i+8, n):
        G.append(math.dist(x[7], x[g]))
        if(min>G[i]):
            min=G[i]
    for h in range(i+9, n):
        H.append(math.dist(x[8], x[h]))
        if(min>H[i]):
            min=H[i]
    for k in range(i+10, n):
        K.append(math.dist(x[9], x[k]))
        if(min>K[i]):
            min=K[i]
print(min) 