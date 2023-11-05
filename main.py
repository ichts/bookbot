def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_counted = count_letter(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    print("")
    print("")

    letter_count_list = list(letter_counted.values())
    letter_count_list.sort(reverse=True)
    for count in letter_count_list:
        for letter in letter_counted:
            if letter.isalpha() and count == letter_counted[letter]:
                print(f"The {letter} character was found {count} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def count_words(str):
    words = str.split()
    return len(words)


def count_letter(text):
    letter_count = {}

    for char in text.lower():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    return letter_count


main()
