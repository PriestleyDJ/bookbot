def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    
    print("__________Beginning Of Report__________")
    print(f"{word_count} words found in this book.")
    chars_dict = get_chars_dict(text)
    print_chars_dict(chars_dict)
    print("__________End Of Report__________")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def get_word_count(text):
    words = text.split()
    return len(words)
    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def print_chars_dict(c_dict):
    c_sorted = sorted(c_dict.items(), key=lambda item: item[1], reverse=True)
    for c in c_sorted:
        if c[0].isalpha():
            print(f"The '{c[0]}' was found {c_dict[c[0]]} times.")

main()