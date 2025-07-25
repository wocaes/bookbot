from stats import word_count

from stats import letter_count

from stats import sorted_dict

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    print(f"{word_count(book_text)} words found in the document")
    print(letter_count(book_text))
    print(sorted_dict(letter_count(book_text)))

main()
