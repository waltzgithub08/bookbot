from stats import get_word_count
from stats import get_character_count
from stats import sort_result_set
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]


def get_book_text(filepath):
    file_contents = ""
    
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents

  
def main():
    file_contents = get_book_text(file_path)
    
    num_words = get_word_count(file_contents)
    #print(f"{num_words} words found in the document")
    
    char_count = get_character_count(file_contents)
    #print(char_count)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    result_set = sort_result_set(char_count)
    
    for item in result_set:
        print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")

    
main()