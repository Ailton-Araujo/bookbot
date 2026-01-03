import sys
from stats import count_words, create_char_dict, print_sorted_char_dict



def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    word_count = count_words(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count_dict = create_char_dict(file_path)
    print_sorted_char_dict(char_count_dict)
    print("============= END ===============")

main()