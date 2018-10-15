
def fibo(n, a = 0, b = 1, fib = []):
    if b < n:
        fib.append(b)
        a, b = b, a + b
    else:
        return fib
    return fibo(n, a, b, fib)

print(fibo(20)) 

  



