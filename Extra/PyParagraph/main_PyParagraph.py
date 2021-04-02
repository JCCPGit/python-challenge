## PyParagraph

# import required modules
import os
import string
from collections import Counter
import re

# paths
paragraph_path = os.path.join("Resources", "paragraph_3.txt")

with open(paragraph_path, "r") as datafile:
    
# approximate word count
    data = datafile.read()
    words = data.split()
    number_words = len(words)

# approximate sentece count
    sentences = re.split("(?<=[.!?]) +", data)
    number_sentences = len(sentences)

# approximate leter count
    number_letters = len(data)
    letter_count_perword = round(number_letters / number_words, 0)
    
# aproximate sentence length
    sentence_length = round(number_words / number_sentences, 0)

# print analysis 
print("----------------")
print(data)
print("----------------")
print(f"Approximate Word Count: {number_words}")
print(f"Approximate Sentence Count: {number_sentences}")
print(f"Average Letter Count: {letter_count_perword}")
print(f"Average Sentence Length: {sentence_length}")
print("----------------")




# ----

# helper function to read a file and return the data
# def load_file(filepath):
    # with open(filepath, "r") as paragraph_file_handler:
        # return paragraph_file_handler.read().split()

# grap the text for a paragraph
# word_list = load_file(paragraph_path)

# create a set of unique words from the paragraph
# paragraph = set()

# create a set of unique words from the paragraph
# for token in word_list:
    # paragraph.add(token.split(',')[0].split('.')[0])
# print(paragraph)

# print(word_list)