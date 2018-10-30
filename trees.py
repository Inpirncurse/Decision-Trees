import copy
import fileinput
import time
import pprint as pp
import random
import numpy as np
import math 

def add_attribute(string, attributes):
    string = string.split(' ')
    name = string[0].replace(' ','')
    if not attributes:
        attributes[0] = {'name': name, 'values':[]}
        for element in string[1:]:
            attributes[0]['values'].append(element.replace(',','').replace(' ','').replace('}','').replace('{',''))
    else:
        key = max(attributes, key=int) + 1
        attributes[key] = {'name': name, 'values':[]}
        for element in string[1:]:
            attributes[key]['values'].append(element.replace(',','').replace(' ','').replace('}','').replace('{',''))

def entropy(data_table, att):
    last = list(att.keys())[-1]
    last_att = att[last]
    values = {}
    #print('EL LAST ', last_att['values'])
    
    for lel in last_att['values']:
        values[lel] = 0

    for row in data_table:
        values[row[-1]] += 1  

    #print(values)

    total = len(data_table)
    #print(total)
    entropy = 0
    for key, value in values.items():
        log2 = math.log((value/total), 2.0)
        log2 *= -(value/total)
        entropy += log2

    print("Entropy: \n",entropy)
    return entropy

    



def information_gain(data, attribute, entropy, attributes):
    entropy_children = 0.0
    total = len(data)
    index = [k for k,v in attributes.items() if v['name'] == attribute]
    for value in attributes[index[0]]['values']:
        split = [row for row in data if value == row[index[0]]]
        #pp.pprint(split)
        quantity = len(split)
        w_average = quantity / total
        #pp.pprint(quantity)


def main():
    file_input = fileinput.input()
    attributes = {}

    data = []
    for line in file_input:
        if(line[0] != '%' and line != '\n'):
            if(line[0:10] == '@attribute' or line[0:10] == '@ATTRIBUTE'):
                add_attribute(line[11:].replace('\n',''), attributes)
            elif(line[0:5] != '@data' and line[0:5] != '@DATA' and line[0:9] != '@relation' and line[0:9] != '@REALTION'):
                data.append(line.replace('\n','').split(','))

    information_gain(data, 'outlook', 0.5, attributes)

    print('Data: ')
    pp.pprint(data)
    print("Attributes: ")
    pp.pprint(attributes)
    
    #entropy
    entropy(data, attributes)

if __name__ == "__main__":
    main()
