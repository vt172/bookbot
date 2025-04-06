from stats import word_counter
from stats import char_counter
from stats import dict_sorter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents




def main(filepath):
    txt = get_book_text(filepath)
    unsorted = char_counter(txt)
    sorted = dict_sorter(unsorted)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(txt)} total words")
    print("--------- Character Count -------")
    for dic in sorted:
        if dic["character"].isalpha():
            print(f"{dic["character"]}: {dic["number"]}")
    print("============= END ===============")

main("books/frankenstein.txt")
