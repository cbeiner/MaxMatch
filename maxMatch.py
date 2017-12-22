import json
import os, sys
import numpy as np

# Just a simple recursive function to read the embedded lists
def read_embedded_list(this_list):
    words = []
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



def max_match(unparsed_word, dictionary, parse_start):
    # string is empty
    if not unparsed_word:
        return []
    # else recursively parse string
    for idx in range(parse_start, 0, -1):
        first_word = unparsed_word[:idx]
        remainder = unparsed_word[idx:]
        if dictionary.get(first_word):
            return [first_word, max_match(remainder, dictionary, len(remainder))]
    # so the first word is a one-character word
    first_word = unparsed_word[0]
    remainder = unparsed_word[1:]
    return [first_word, max_match(remainder, dictionary, len(remainder))]


def modified_max_match(word, dictionary):
    # this utilizes the parse_start variable to allow the algorithm to return
    # multiple segmentations of the word, even if it returns earlier
    length = len(word)
    segmentations = []
    # The idea here is that the greedy version will exit the loop when we reach the first
    # segment that is a word - which is a problem
    for idx in range(length, 0, -1):
        # So instead, we go through the whole segment and get all valid segmentations
        segmentations.append(read_embedded_list(max_match(word, dictionary, idx)))
    segmentations = np.unique(np.array(segmentations))
    # Then we return the segmentation with the largest character-to-word ratio
    return segmentations[np.argmax(np.array([length/len(segment) for segment in segmentations]))]




def main():
    english_words = load_words()
    # Some trending hashtags
    word_list = ["bananamoon", "6yearswithkai", "foxnews", "amazongiveaway", "ohmygirl", "mkjbeastmode", "metoo"]
    print("Word segmentation using the greedy MaxMatch algorithm: ")
    for word in word_list:
        print(word + " === " + read_embedded_list(max_match(word, english_words, len(word))))
    print('\n' + "Word segmentation using a heuristic MaxMatch algorithm: ")
    for word in word_list:
        print(word + " === " + modified_max_match(word, english_words) )
    print('\n')

if __name__ == '__main__':
    main()
