import null as null
import pandas as pd
import spacy
import xlsxwriter
import os

parsing_excel = pd.read_excel(r'C:\Users\Jim Lee\Desktop\競品分析\test_parse.xlsx', sheet_name="parsing")
titles = pd.read_excel(r'C:\Users\Jim Lee\Desktop\競品分析\test_parse.xlsx', sheet_name="parsing", usecols="A")
parsed_titles = pd.read_excel(r'C:\Users\Jim Lee\Desktop\競品分析\test_parse.xlsx', sheet_name="parsing", usecols="B")
parsed_key_list = []
row_list = []
sum_for_each_key = []

print(parsing_excel)


# iterate through each column to find all keywords to be named as the title for columns
for i in range(titles.shape[0]):

    parsed_title = str(parsed_titles.values[i][0]).split("|")
    for j in range(len(parsed_title)):
        if parsed_title[j] not in parsed_key_list:
            parsed_key_list.append(parsed_title[j])


print(parsed_key_list)

# write each row/title
for i in range(parsed_titles.shape[0]):
    parsed_title = str(parsed_titles.values[i][0]).split("|")
    current_row = []
    for j in range(len(parsed_key_list)):
        if parsed_key_list[j] in parsed_title:
            current_row.append(1)
        elif parsed_key_list not in parsed_title:
            current_row.append(0)
    row_list.append(current_row)
    #print(current_row)

# tally up for all keywords
for i in range(len(parsed_key_list)):
    sum = 0
    for j in range(len(row_list)):
        sum += row_list[j][i]
    sum_for_each_key.append(sum)

print(sum_for_each_key)
print(len(sum_for_each_key) == len(parsed_key_list))







# write to another excel
workbook = xlsxwriter.Workbook(r"C:\Users\Jim Lee\Desktop\競品分析\new.xlsx")
worksheet = workbook.add_worksheet()

key_plus_count = [parsed_key_list, sum_for_each_key]

for row_num, row_data in enumerate(key_plus_count):
    for col_num, col_data in enumerate(row_data):
        worksheet.write(row_num, col_num, col_data)

workbook.close()



