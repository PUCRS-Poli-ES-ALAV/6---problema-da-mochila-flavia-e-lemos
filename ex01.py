def fibo_rec(n):
    if n<=1:
        return n
    else:
        a = fibo_rec(n-1)
        b = fibo_rec(n-2)
        return a + b

def fibo (n):
    f = []
    f.append(0)
    f.append(1)
    for i in range (2,n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

def memoized_fibo(n):
    f = [-1] * (n + 1)
    return lookup_fibo(f,n)

def lookup_fibo(f, n):
    if f[n]>=0:
        return f[n]
    if n<=1:
        f[n] = n
    else:
        f[n] = lookup_fibo(f, n-1) + lookup_fibo(f,n-2)
    return f[n]

print (fibo_rec(4))
print (fibo(4))  
print(memoized_fibo(4))