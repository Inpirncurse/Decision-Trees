import copy
import fileinput
import time
import pprint as pp
import random

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

def entropy(data):
    value = random.uniform(0.0, 1.0)
    print(value)
    return value


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

if __name__ == "__main__":
    main()
