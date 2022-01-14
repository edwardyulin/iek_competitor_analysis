import pandas as pd
import spacy
import xlsxwriter

parsing_excel = pd.read_excel(r'C:\Users\Jim Lee\Desktop\競品分析\test_parse.xlsx')
titles = pd.read_excel(r'C:\Users\Jim Lee\Desktop\競品分析\test_parse.xlsx', usecols="A")
parsed_titles = pd.read_excel(r'C:\Users\Jim Lee\Desktop\競品分析\test_parse.xlsx', usecols="B")
parsed_key_list = []
row_list = []
sum_for_each_key = []

# parse titles
nlp = spacy.load("zh_core_web_sm")

# iterate through each column to find all keywords to be named as the title for columns
# WITH AUTOMATIC PARSING FROM SPACY
for i in range(titles.shape[0]):
    title_to_parse = nlp(titles.values[i][0])
    # print(title_to_parse.text)
    for token in title_to_parse:
        parsed_key_list.append(token.text)


print(parsed_key_list)

# write each row/title
for i in range(parsed_titles.shape[0]):
    title_to_parse = nlp(titles.values[i][0])
    parsed_title = []
    # print(title_to_parse.text)
    for token in title_to_parse:
        parsed_title.append(token.text)
    current_row = []
    for j in range(len(parsed_key_list)):
        if parsed_key_list[j] in parsed_title:
            current_row.append(1)
        elif parsed_key_list not in parsed_title:
            current_row.append(0)
    row_list.append(current_row)
    # print(current_row)

# tally up for all keywords
for i in range(len(parsed_key_list)):
    sum = 0
    for j in range(len(row_list)):
        sum += row_list[j][i]
    sum_for_each_key.append(sum)

print(sum_for_each_key)
print(len(sum_for_each_key) == len(parsed_key_list))

"""
# TODO: PRINTING TO EXCEL
df = pd.DataFrame(columns=parsed_key_list)
writer = pd.ExcelWriter(parsing_excel, engine='xlsxwriter')
df.to_excel(writer, sheet_name="results")
writer.save()
"""



