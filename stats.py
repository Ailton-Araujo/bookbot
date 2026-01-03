def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def count_words(file_path):
    text = get_book_text(file_path)
    words = text.split()
    return len(words)

def create_char_dict(file_path):
    text = get_book_text(file_path)
    characters_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in characters_dict:
                characters_dict[char] += 1
            else:
                characters_dict[char] = 1
    return characters_dict

def print_sorted_char_dict(char_dict):
    sorted_items = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_items:
        print(f"{char}: {count}")