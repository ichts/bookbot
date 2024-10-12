def main():
    book_path = "books/frankenstein.txt"
    content = get_book_txt(book_path)
    number_of_words = count_words(content)

    char_frequences = count_character(content)
    # char_frequences.items().sort(reverse=True, key=sort_on)

    print(f"--- Book report of {book_path} ---")

    print(f"{ number_of_words } words found in the document\n")


    char_list = char_dict_to_list(char_frequences)

    for i in char_list:
        if i["char"].isalpha():
            print(f"The '{i[ "char" ]}' was found {i["num"]} times ")


    print(f"--- End report ---")



def sort_on(dict):
    return dict["num"]

def char_dict_to_list(char_frequences):
    list = []
    for ch in char_frequences:
        list.append({"char":ch, "num": char_frequences[ch]})

    list.sort(reverse=True, key=sort_on)
    return list




def get_book_txt(path):
    with open(path) as f:
        return f.read()


def count_words(content):
    words = content.split()
    return len(words)

def count_character(content):
    char_frequences = {}
    words = content.split();
    for word in words:
        for c in word.lower():
            if c in char_frequences:
                char_frequences[c] = char_frequences[c] + 1
            else:
                char_frequences[c] = 1

    return char_frequences



main()
