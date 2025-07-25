def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def word_count(book_text):
    counter = 0
    with open(book_text) as f:
        words = f.read() 
        num_words = words.split()
        for word in num_words:
            counter += 1
    return counter

"""def main():
    book_text = "books/frankenstein.txt"
    print(word_count(book_text))

main()"""

            
    
def main():
    file_path = "books/frankenstein.txt"
    book_text = "books/frankenstein.txt"
    print(f"{word_count(book_text)} words found in the document")

main()
