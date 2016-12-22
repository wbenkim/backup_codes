def returnTotal():
    i = [1,3,4,7]
    sumTotal = 0
    for k in i:
        sumTotal += k
    return sumTotal

def sumOfN(n):
    totalSum = 0
    for i in range(1,n+1):
        totalSum += i
    return totalSum

print sumOfN(10)
print returnTotal()
