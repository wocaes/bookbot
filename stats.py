# counts words

def word_count(book_text):
    words = book_text.split() 
    return len(words)

# counts letters

def letter_count(book_text):
    book_text = book_text.lower()
    dict_count = {}
    
    for char in book_text:
        if char in dict_count:
            dict_count[char] += 1
        else:
            dict_count[char] = 1
    return dict_count


