import sys

from stats import word_count

from stats import letter_count

from stats import sorted_dict

#define CLI arguments
args = sys.argv


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    #instruct how to use
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = args[1]
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
