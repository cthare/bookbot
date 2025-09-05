import sys
from stats import count_words, count_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    with open(path_to_file) as f:
        file_contents = f.read()

    word_report = count_words(file_contents)
    character_report = count_characters(file_contents)

    print("============ BOOKBOT ============")
    print(f"--- Begin report of {path_to_file} ---")
    print("----------- Word Count ----------")
    print(f"{word_report} words found in the document")
    print("--------- Character Count -------")
    for i in character_report:
        print(f"{i}: {character_report[i]}")

    print("============= END ===============")

main()
