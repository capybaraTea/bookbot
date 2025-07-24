from stats import get_word_count, get_char_appearance, sort_dictionary, sort_on
import sys

def get_book_text(filepath):
    file = open(filepath, "r")
    file_contents = file.read()
    return file_contents

def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    char_counts = get_char_appearance(text)
    sorted_counts = sort_dictionary(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_counts:
        if dict["name"].isalpha():
            print(f"{dict["name"]}: {dict["num"]}")
    
    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
