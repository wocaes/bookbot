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


#returns a sorted list of dictionaries
def sort_on(dict_count):
    return dict_count["num"]

def sorted_dict(dict_count):
    final_list = []
    for char in dict_count:
        #key = char
        #value = dict_count[char]
        sorted_dict = {"char": char, "num": dict_count[char]}
        final_list.append(sorted_dict)
    final_list.sort(reverse=True, key=sort_on)
    return final_list


    