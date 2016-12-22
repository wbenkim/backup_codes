def factorial_iterative(n):
    x = 1
    li = list(range(1,n+1))
    for each in li:
        x = x * each
    return x

print factorial_iterative(5)
            
