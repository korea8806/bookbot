from string import ascii_lowercase

def lettercount(text):
    letter_dict = dict()
    for c in ascii_lowercase:        
        letter_dict[c] = text.lower().count(c)
    return letter_dict

def wordcount(text):
    return len(text.split())

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"{wordcount(file_contents)} words found in the document\n\n")
        for key, value in lettercount(file_contents).items(): 
            print(f"The '{key}' character was found {value} times")

main()