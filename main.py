from stats import word_count

from stats import letter_count

from stats import sorted_dict

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    final_view_list = sorted_dict((letter_count(book_text)))
    for item in final_view_list:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
