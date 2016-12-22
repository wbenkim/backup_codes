def binary_converter(x):
    if x == 0:
        return "Invalid conversion"
    elif x == 62:
        return "Inavlid conversion"
    elif x < 0:
        return "Input below 0 not allowed"
    elif x > 255:
        return "Input above 255 not allowed"
    else:
        return bin(x)[2:]

print binary_converter(10)
