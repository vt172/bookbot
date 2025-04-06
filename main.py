from stats import word_counter
from stats import char_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(filepath):
    print(word_counter(get_book_text(filepath)))
    print(char_counter(get_book_text(filepath)))

main("books/frankenstein.txt")

## Next time, start here:
## https://www.boot.dev/lessons/b82a6805-17c9-4b1c-a1e6-def866faa7e6