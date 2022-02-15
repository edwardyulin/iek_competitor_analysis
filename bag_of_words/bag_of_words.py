import numpy as np
import pandas as pd

"""
Bag-of-Words model for text classification
   - Extract keywords from given information and tally up sum for each keyword
   - Each tallied up total will be the lower bound of actual count of keywords 
     (since BoW model only recognize keywords if exists in the given info.)

PROS: easy, fast because no training required, don't require NLP
CONS: inaccurate because words need to be exact, no order involved
"""


input_excel = pd.ExcelFile(r'C:\Users\Jim Lee\PycharmProjects\iek_competitor_analysis\test_parse.xlsx')  # or use other .xlsx files
data = pd.read_excel(input_excel, sheet_name="for_training", usecols="C:N")
keys = pd.read_excel(input_excel, sheet_name="for_training", usecols="P:AN")
data_list = list(data.columns.values)
key_list = list(keys.columns.values)
print(data_list)
print(key_list)
size_of_data = data.shape[0]


all_data = []
rows = []  # count of keywords for each article (makes up a table)
total = []  # tallied up total for each key
total_with_key = []


# parse all tokens for all articles
for i in range(size_of_data):
    text = data.loc[i]  # columns A:N
    data_text_list = list(text)
    #print(data_text_list)
    data_for_i = '|'.join(map(str, data_text_list))
    #print(data_for_i)
    all_data.append(data_for_i)

print(all_data)


# draw a table with zeroes for all counts
for i in range(size_of_data):
    current_row = []
    for j in range(len(key_list)):
        current_row.append(0)
    rows.append(current_row)
    #print(rows)

# match tokens with keys


def matching(key, data, key_count, data_count):
    if key_count < len(key):
        if key[key_count] == data[data_count]:
                key_count += 1
                data_count += 1
                matching(key, data, key_count, data_count)

    elif key_count == len(key):
        print("found a match: ", key, data)
        key_index = key_list.index(key)
        data_index = all_data.index(data)
        if rows[data_index][key_index] == 0:
            rows[data_index][key_index] = 1


# call matching
for data in all_data:
    for key in key_list:
        key_count = 0
        data_count = 0
        matching(key, data, key_count, data_count)

# tally up total of appearance for each keyword
for i in range(len(key_list)):
    sum = 0
    for j in range(size_of_data):
        sum += rows[j][i]
    total.append(sum)

print(key_list)
print(total)

# combine keywords with sum to create a new list
for i in range(len(key_list)):
    to_add = key_list[i], total[i]
    total_with_key.append(to_add)

print(total_with_key)

#TODO: output to excel




