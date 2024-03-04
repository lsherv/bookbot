def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_letter_count(text)
    print(text)
    print(f'Total wordcount is {word_count}')
    print(char_count)
     

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    letters_count = {}
    letters = list(text.lower())
    
    for char in letters:
        if char == ' ':
            continue
        elif char not in letters_count:
            letters_count[char] = 1
        else:
            letters_count[char] += 1
    return letters_count

main()
