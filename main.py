from stats import word_counter
from stats import char_counter
from stats import dict_sorter
import sys

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
    except Exception as e:
        print(e)
        print("Please make sure that the filepath is valid.")
        sys.exit(1)

    return file_contents

def main(arg):
    if len(arg) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = arg[1]

    # begining of the program
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


main(sys.argv)
