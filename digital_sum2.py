def digital_sum(list_data):
    sumTotal = 0
    for x in list_data:
        if x > 10:
            for y in str(x):
                sumTotal = sumTotal + int(y)
        else:
            sumTotal = sumTotal + x
    return sumTotal
        
print digital_sum([1,2,30,55])
