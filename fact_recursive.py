'''def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print factorial(5)'''
prices = {"banana":4,"apple":2,"orange":1.5,"pear":3}
stock = {"banana":6,"apple":0,"orange":32,"pear":15}

for x in prices:
    print "Prices: %.f" % prices[x]
