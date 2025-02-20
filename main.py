alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def load_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    low_text = text.lower()
    for char in low_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars 

def printout(words, chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    
    for key in chars:
        if key in alphabet:
            print(f"The '{key}' character was found {chars[key]} times")
        

def main():
    total_words = word_count(load_text())
    chars_dict = char_count(load_text())

    printout(total_words, chars_dict)
    print("--- End report ---")

main()