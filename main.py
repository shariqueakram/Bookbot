def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)
    return file_contents

def word_count(input):
    word_count = len(input.split())
    print(word_count)
    return word_count

def count_characters(input):
    chars = {}
    for x in input:
        lower_cased_text = x.lower()
        if lower_cased_text in chars:
            chars[lower_cased_text] += 1
        else:
            chars[lower_cased_text] = 1
    return chars

if __name__ == '__main__':
    text = main()
    word_count = word_count(text)
    char_count = count_characters(text)
    for key, value in char_count.items():
        if (key.isalpha()):
            print(f"The '{key}' character was found '{value}' times")

    
