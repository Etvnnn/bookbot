from stats import word_count
from stats import letter_count
from stats import sort_characters
import sys

def get_book_text(file_path):
    text = ""
    with open(file_path) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    count = word_count(text)
    characters = letter_count(text)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book}")
    print ("----------- Word Count ----------")
    print(f"Found {count} total words")
    # When printing the report
    print("--------- Character Count -------")
    sorted_chars = sort_characters(characters)
    # Now loop through the sorted list of dictionaries
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()