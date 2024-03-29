import re

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        print(f"{num_words} words found in the document")
        char_occurance = count_occurance_of_chars(file_contents)
        print("The following are found in the document:")
        print(char_occurance)

def get_num_words(text):
    words = text.split()
    return len(words)

def count_occurance_of_chars(text):
    lower_text = text.lower()
    letter_count_dict = {}
    for i in range(len(lower_text)):
        if lower_text[i] in letter_count_dict:
            letter_count_dict[lower_text[i]] += 1
        else:
            letter_count_dict[lower_text[i]] = 1

    return letter_count_dict



main()