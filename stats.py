def word_counter(text):
    word_list = text.split()
    word_counter = 0
    for word in word_list:
        word_counter += 1
    return f"{word_counter} words found in the document"

def char_counter(text):
    char_counter = {}
    for char in text:
        char = char.lower()
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter
