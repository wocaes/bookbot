def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def word_count(book_text):
    words = book_text.split() 
    return len(words)
    
    
def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    print(f"{word_count(book_text)} words found in the document")

main()
