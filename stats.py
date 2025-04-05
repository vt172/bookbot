def word_counter(text):
    word_list = text.split()
    word_counter = 0
    for word in word_list:
        word_counter += 1
    return f"{word_counter} words found in the document"