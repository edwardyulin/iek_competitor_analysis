import pandas as pd
import spacy
import xlsxwriter


class AutoParser:
    """Automatically parse titles using SpaCy library"""

    # iterate through each column to find all keywords to be named as the title for columns
    # WITH AUTOMATIC PARSING FROM SPACY
    def parse_title(self, titles, all_keys, nlp):
        for i in range(titles.shape[0]):
            title_to_parse = nlp(str(titles.values[i][0]))
            # print(title_to_parse.text)
            for token in title_to_parse:
                all_keys.append(token.text)
        # all keys
        #print(all_keys)

    # write each row/title
    def get_each_title_count(self, titles, all_keys, keys_by_arti, count_by_arti, nlp):
        for i in range(titles.shape[0]):
            title_to_parse = nlp(str(titles.values[i][0]))
            current_arti_keys = []
            # print(title_to_parse.text)
            for token in title_to_parse:
                current_arti_keys.append(token.text)
            #print(current_arti_keys)
            keys_by_arti.append(current_arti_keys)
            current_arti_count = []
            for j in range(len(all_keys)):
                if all_keys[j] in current_arti_keys:
                    current_arti_count.append(1)
                elif all_keys not in current_arti_keys:
                    current_arti_count.append(0)
            count_by_arti.append(current_arti_count)
            #print(current_arti_count)

    # tally up for all keywords
    def sum_up_counts(self, all_keys, row_list, sum_for_each_key):
        for i in range(len(all_keys)):
            sum = 0
            for j in range(len(row_list)):
                sum += row_list[j][i]
            sum_for_each_key.append(sum)

        #print(sum_for_each_key)
        #print(len(sum_for_each_key) == len(all_keys))

    def pipeline(self):
        input_excel = pd.ExcelFile(r'C:\Users\Jim Lee\Desktop\競品分析\test_parse.xlsx')
        titles = pd.read_excel(input_excel, sheet_name="for_training", usecols="C")

        sum_for_each_key = []
        all_keys = []
        keys_by_arti = []
        count_by_arti = []

        nlp = spacy.load("zh_core_web_lg")

        self.parse_title(titles=titles,
                         all_keys=all_keys,
                         nlp=nlp)
        self.get_each_title_count(titles=titles,
                                  all_keys=all_keys,
                                  keys_by_arti=keys_by_arti,
                                  count_by_arti=count_by_arti,
                                  nlp=nlp)
        self.sum_up_counts(all_keys=all_keys,
                           row_list=count_by_arti,
                           sum_for_each_key=sum_for_each_key)

        # all_keys = [key1, key 2, key 3, ...]
        # sum_for_each_key = [# of key 1, # of key 2, # of key 3, ...]
        # keys_by_arti = [[key1, key2, key3], [key1, key 4], ....]
        # count_by_arti = [[0,0,1,...], [0,1,0,...], ....]
        print(keys_by_arti)
        return all_keys, sum_for_each_key, keys_by_arti, count_by_arti


    #TODO: PRINT OUTPUT TO EXCEL