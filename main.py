def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

from stats import word_count    

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    print(f"{word_count(book_text)} words found in the document")

main()
