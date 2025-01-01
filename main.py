path_to_file = "books/frankenstein.txt"

def count_words(book_file_stream):
    word_count = book_file_stream.split()

    return len(word_count)


def count_characters(book_file_stream):
    word_list = book_file_stream.lower().split()
    character_list = {}

    for i in word_list:
        for y in i:
            if y.isalpha() == True:
                if y in character_list:
                    character_list[y] += 1
                else:
                    character_list[y] = 1
    
    return dict(sorted(character_list.items()))


def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    word_report = count_words(file_contents)
    character_report = count_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_report} words found in the document")
    print("")
    for i in character_report:
        print(f"The '{i} character was foudn {character_report[i]} times")

    print("--- End report ---")

main()
