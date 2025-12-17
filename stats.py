from collections import Counter

def get_book_text(path : str):
    with open(path) as f:
        contents = f.read()
    return contents

def get_num_words(path : str):
    return len(get_book_text(path).split())

def get_char(path : str):
    return Counter(get_book_text(path).lower())