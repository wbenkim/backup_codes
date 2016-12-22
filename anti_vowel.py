def anti_vowel(text):
    result = text
    for char in text:
        if char in "aeiouAEIOU":
            result = result.replace(char, '')
    return result

print anti_vowel("aeijhhjouAEKJKJKIOU")
