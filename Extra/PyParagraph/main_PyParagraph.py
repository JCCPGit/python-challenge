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
    number_letters = len(data) - data.count(" ")
    letter_count_perword = round(number_letters / number_words, 1)
      
# aproximate sentence length
    sentence_length = round(number_words / number_sentences, 1)

# print analysis 
print("----------------")
print(data)
print("----------------")
print(f"Approximate Word Count: {number_words}")
print(f"Approximate Sentence Count: {number_sentences}")
print(f"Average Letter Count: {letter_count_perword}")
print(f"Average Sentence Length: {sentence_length}")
print("----------------")
