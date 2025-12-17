from stats import get_num_words, get_char
import sys

def __main__():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    PATH = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(PATH)} total words")
    print("--------- Character Count -------")
    d = sorted(get_char(PATH).items(), reverse = True, key = lambda item: item[1])
    for (key, val) in d:
        if key.isalpha():
            print(f"{key}: {val}")

    print(sys.argv)

__main__()



