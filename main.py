def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_letters = count_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in sort_letter_count(num_letters):
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was cound {item["num"]} times")

    print("--- End report ---")

def get_word_count(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    letter_count = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letter_count:
            letter_count[lowered] += 1
        else:
            letter_count[lowered] = 1
    return letter_count

def sort_on(d):
    return d["num"]

def sort_letter_count(letters):
    sorted_list = []
    for letter in letters:
        sorted_list.append({"char": letter, "num": letters[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()