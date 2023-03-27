n = int(input())
k = int(input())

def f(n):
    f0 = 1;
    f1 = 1;
    fn = 2;
 
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return 1;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;

k=2*k
print((n*f(k))%1000000007)