import csv

def tradition_to_simplify():
    ch_dict = dict()
    with open('data/zh2Hans.csv', 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, delimiter = ';')
        for row in reader: 
            ch_dict[row['繁体']] = row['简体']
    #print(li_of_dicts)
    return ch_dict

def simplify_to_tradition():
    ch_dict = dict()
    with open('data/zh2Hant.csv', 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, delimiter = ';')
        for row in reader: 
            ch_dict[row['简体']] = row['繁体']
    #print(li_of_dicts)
    return ch_dict
    