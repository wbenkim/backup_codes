def binary_converter(x):
    if x == 0:
        return "0"
    elif x == 62:
        return "111110"
    elif x < 0:
        return "Invalid input"
    elif x > 255:
        return "Invalid input"
    else:
        return bin(x)[2:]