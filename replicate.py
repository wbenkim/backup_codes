def replicate_recur(n, values):
    x = []
    if n == 0:
        return x
    else:
        return [values] + replicate_recur(n-1, values) 
        
print(replicate_recur(9, "3"))
