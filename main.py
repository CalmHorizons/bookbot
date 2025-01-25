def count_words_in_book(book):
    book_length = len(book.split())
    return book_length

def count_characters_book(book):
    lower_case_book = book.lower()
    character_dictionary = {}
    from string import ascii_lowercase as alc
    for char in alc:
        total_count = lower_case_book.count(char)
        character_dictionary[char] = total_count
    #Append space since the question marks are arsy
    #character_dictionary[" "] = lower_case_book.count(" ")
    return character_dictionary

def print_report(book):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words_in_book(book)} words found in the document")
    character_data = count_characters_book(book)
    for character in character_data:
        print(f"The '{character}' character was found {character_data[character]} times")

file_path = "books/frankenstein.txt"
with open(file_path) as f:
    file_contents = f.read()
    #print(file_contents)
    #print(f"Number of Words:{count_words_in_book(file_contents)}")
    #print(f"Character Counts: {count_characters_book(file_contents)}")
    print_report(file_contents)
