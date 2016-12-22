def digital_sum_list(list_data):
    total = 0
    for x in list_data:
        if x >= 10:
            for n in str(x):
                total = total + int(n)
        else:
            total = total + x
    return total

print digital_sum_list([10,1,23,45])
