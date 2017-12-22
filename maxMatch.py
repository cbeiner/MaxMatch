import json
import os, sys

# Just a simple recursive function to read the embedded lists
def read_embedded_list(this_list):
    if len(this_list) == 0:
        return ""
    else:
        return this_list[0] + " " + read_embedded_list(this_list[1])


def load_words():
    # load json file of all english words
    try:
        filename = os.path.dirname(sys.argv[0])+"\\"+"word_dictionary.json"
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)


def max_match(unparsed_word, dictionary):
    # string is empty
    if not unparsed_word:
        return []
    # else recursively parse string
    for idx in range(len(unparsed_word), 0, -1):
        first_word = unparsed_word[:idx]
        remainder = unparsed_word[idx:]
        if dictionary.get(first_word):
            return [first_word, max_match(remainder, dictionary)]
    # so the first word is a one-character word
    first_word = unparsed_word[0]
    remainder = unparsed_word[1:]
    return [first_word, max_match(remainder, dictionary)]


def main():
    english_words = load_words()
    print(read_embedded_list(max_match("agreatplace", english_words)))
    print(read_embedded_list(max_match("pleaseandthankyou", english_words)))
    print(read_embedded_list(max_match("boysrule", english_words)))
    print(read_embedded_list(max_match("metoo", english_words)))

if __name__ == '__main__':
    main()
