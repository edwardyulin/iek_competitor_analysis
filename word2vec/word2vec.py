import zh_core_web_lg
import pandas as pd
import spacy
import numpy as np

"""
Word2Vec Model: compare vectors from each parsed words with vectors from each keyword by dot product (how similar they are)
PROS: reads not only the exact wording
CONS: inaccurate, initial parsing of titles (and information) is off
"""


input_excel = pd.ExcelFile(r'C:\Users\Jim Lee\Desktop\競品分析\test_parse.xlsx')  # or use other .xlsx files
data = pd.read_excel(input_excel, sheet_name="for_training", usecols="C:N")
keys = pd.read_excel(input_excel, sheet_name="for_training", usecols="P:AN")
data_list = list(data.columns.values)
key_list = list(keys.columns.values)
print(data_list)
print(key_list)
size_of_data = data.shape[0]


all_data = []
all_keys = []
rows = []  # count of keywords for each article (makes up a table)
total = []  # tallied up total for each key
total_with_key = []

nlp = zh_core_web_lg.load()

# draw a table with zeroes for all counts
for i in range(size_of_data):
    current_row = []
    for j in range(len(key_list)):
        current_row.append(0)
    rows.append(current_row)

# parse all tokens for all articles
for i in range(size_of_data):
    text = data.loc[i]  # columns A:N
    data_text_list = list(text)
    #print(data_text_list)
    data_for_i = '|'.join(map(str, data_text_list))
    #print(data_for_i)
    all_data.append(data_for_i)

print(all_data)

for i in range(len(all_data)):
    title_to_parse = nlp(all_data[i])
    current = []
    # print(title_to_parse.text)
    for token in title_to_parse:
        current.append(token.text)

    all_keys.append(current)


for words_in_each_article in all_keys:
    for word in words_in_each_article:
        if word == '|' or word == '/':  # also check for other conditions
            words_in_each_article.remove(word)
print(all_keys)

# https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy/

# TODO: compare each word vector with key vector (dot product)
# 1. convert all parsed words to vectors
all_words_vectors = []
for words_in_each_article in all_keys:
    current_article = []
    for word in words_in_each_article:
        current_word_vector = nlp(word).vector
        current_article.append(current_word_vector)
    all_words_vectors.append(current_article)

# 2. find vectors for each key
all_keys_vectors = []
for key_vector in key_list:
    temp_key_vector = nlp(key_vector).vector
    all_keys_vectors.append(temp_key_vector)

# 3. dot product each vectors from parsed words with key vectors
all_dots = []
for arti in all_words_vectors:
    dots_for_arti = []
    for word in arti:
        dots_for_word = []
        for key in all_keys_vectors:
            word_key_pair = np.dot(word, key)
            dots_for_word.append(word_key_pair)
        dots_for_arti.append(dots_for_word)
        #print(len(dots_for_word))
    all_dots.append(dots_for_arti)
    print(len(dots_for_arti))
#print(len(all_dots))
#print(all_dots)

# 4. if the dot product < X, then add 1 to the count for that article
for arti in all_dots:
    for word in arti:
        for word_key_pair in word:
            if abs(word_key_pair) < 2 and word_key_pair != 0:
                print(word_key_pair)
                key_index = word.index(word_key_pair)
                arti_index = all_dots.index(arti)
                rows[arti_index][key_index] = 1

# tally up total of appearance for each keyword
for i in range(len(key_list)):
    sum = 0
    for j in range(size_of_data):
        sum += rows[j][i]
    total.append(sum)


print(total)

# TODO: NEEDS polish, make more robust


# TODO: train vector values with key vector for all known articles
