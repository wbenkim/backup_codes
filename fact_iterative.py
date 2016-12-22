def factorial(n):
    x = 1
    li = list(range(1,n+1))
    for y in li:
        x = x * y
    return x

print factorial(5)
