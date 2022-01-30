def fib_imperative(n):
    sum = 0
    a = 0
    b = 1
    
    if (n == 1):
        sum = 1
    while(n > 1):
        sum = a + b
        a = b
        b = sum
        n = n-1
    
    return sum

