def digital_sum(num):
    return sum( [int(char) for char in str(num) ])

print digital_sum(255)
