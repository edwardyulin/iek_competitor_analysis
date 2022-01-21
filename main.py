from key_parsing import AutoParser
from key_training.training import TitleTraining
import pandas as pd



def main():

    input_excel = pd.ExcelFile(r'C:\Users\Jim Lee\Desktop\競品分析\test_parse.xlsx')
    correct_answers = pd.read_excel(input_excel, sheet_name="for_training", usecols="C,P:AN")
    print(correct_answers)
    all_correct_keys = list(correct_answers.columns.values)
    all_correct_keys.pop(0)
    list_of_correct_answers = correct_answers.values.tolist()  # output nodes
    print(all_correct_keys)
    #correct_keys_by_arti =
    #correct_count_by_arti =

    # call key_parsing
    parser = AutoParser()
    all_parsed_keys, sum_for_each_key, keys_by_arti, count_by_arti = parser.pipeline()
    print(keys_by_arti)  # input nodes
    #print(count_by_arti)


    # then call key_training
    # feed correct answers to training for extraction
    # INPUT: "from auto parsing"
    # OUTPUT: "from correct answer"
    model = TitleTraining()

if __name__ == '__main__':
    main()
