import re

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        list_of_alpha = count_occurance_of_alpha_chars(file_contents)
        num_words = get_num_words(file_contents)
        print_book_report_on_chars(list_of_alpha, num_words, book_path)

def get_num_words(text):
    words = text.split()
    return len(words)

def count_occurance_of_alpha_chars(text):
    alpha_chars_list_of_dict = []
    letter_count_dict = count_occurance_of_chars(text)
    for char in letter_count_dict:
        if not char.isalpha():
            continue
        alpha_chars_list_of_dict.append({
            "name": char, 
            "num_occur":letter_count_dict[char]
            })
    return alpha_chars_list_of_dict

def print_book_report_on_chars(list, num_words, book_path):
    list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for i in range(len(list)):
        print(f"The '{list[i]['name']}' character was found {list[i]['num_occur']} times")
    print("--- End report ---")

def count_occurance_of_chars(text):
    lower_text = text.lower()
    letter_count_dict = {}
    for i in range(len(lower_text)):
        if lower_text[i] in letter_count_dict:
            letter_count_dict[lower_text[i]] += 1
        else:
            letter_count_dict[lower_text[i]] = 1

    return letter_count_dict

def sort_on(dict):
    return dict["num_occur"]

main()