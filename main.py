from stats import count_words, count_characters

path_to_file = "books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    word_report = count_words(file_contents)
    character_report = count_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_report} words found in the document")
    print("")
    for i in character_report:
        print(f"The '{i} character was found {character_report[i]} times")

    print("--- End report ---")

main()
