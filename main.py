def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

main()