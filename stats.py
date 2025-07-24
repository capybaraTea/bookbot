def get_word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_char_appearance(book_text):
    char_dict = {}
    for char in book_text:
        char_lower = char.lower()
        if char_lower in char_dict:
            char_dict[char_lower] += 1
        else:
            char_dict[char_lower] = 1
    return char_dict

def sort_on(items):
    #comment?
    return items["num"]




def sort_dictionary(dict):
    char_counts = list()
    for char in dict:
        temp_dict = {"name": char, "num": dict[char]}
        char_counts.append(temp_dict)
    char_counts.sort(reverse=True,key=sort_on)
    return char_counts
