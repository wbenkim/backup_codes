def anti_vowel(text):
    result = text
    for x in text:
        if x in "aeiouAEIOU":
            result = result.replace(x, "")
    return result

print (anti_vowel("aeioukjkjk"))
