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