import copy
import fileinput
import pprint as pp
import math
import re

def format_attribute(string, attributes):
    # Format the attributes to add it to the dictionary of attributes
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

def entropy(data_table, attributes):
    # Computes the attribute of the given data_table
    last = max(attributes, key=int)
    last_att = attributes[last]
    values = {}

    for lel in last_att['values']:
        values[lel] = 0
    # Counts how many times each value appear in the last column
    for row in data_table:
        values[row[-1]] += 1

    total = len(data_table)
    entropy = 0
    # Compute the entropy
    for key, value in values.items():
        if value > 0:
            log2 = math.log((value/total), 2.0)
            log2 *= -(value/total)
            entropy += log2

    return entropy

def information_gain(data_table, attribute, parent_ent, attributes):
    # Compute the information gain of the given data_table if splitted by the attribute given
    entropy_children = 0
    total = len(data_table)
    index = [k for k,v in attributes.items() if v['name'] == attribute]
    for value in attributes[index[0]]['values']:
        split = [row for row in data_table if value == row[index[0]]]
        quantity = len(split)
        w_average = quantity / total
        entropy_children += w_average * entropy(split, attributes)

    ig = parent_ent - entropy_children
    return ig

def id3_algorithm(data, actual_entropy, attributes, level):
    tabs = "\t"*level
    if actual_entropy == 0:
        print(tabs, "ANSWER: ", data[0][max(attributes, key=int)])
    else:
        ig = 0
        array = [value for key,value in attributes.items()]

        # Iterate over all the attributes except the last one and save the greater value of ig
        for key,element in attributes.items():
            if(key != max(attributes, key=int)):
                aux = information_gain(data, element['name'], actual_entropy, attributes)
                if(aux > ig):
                    ig = aux
                    att = element['name']
                    k = key
        # The greatest value is saved
        for value in attributes[k]['values']:
            print(tabs, att + ": ", value)
            split = [row for row in data if value == row[k]]
            e = entropy(split, attributes)
            id3_algorithm(split, e, attributes, level+1)


def main():
    file_input = fileinput.input()
    attributes = {}

    data = []
    for line in file_input:
        if(line[0] != '%' and line != '\n'):
            if(line[0:10] == '@attribute' or line[0:10] == '@ATTRIBUTE'):
                l = line[11:].replace('\n','').replace('\t',' ')
                format_attribute(re.sub(' +',' ', l), attributes)
            elif(line[0:5] != '@data' and line[0:5] != '@DATA' and line[0:9] != '@relation' and line[0:9] != '@REALTION'):
                data.append(line.replace('\n','').split(','))

    e = entropy(data, attributes)
    id3_algorithm(data, e, attributes, 0)


if __name__ == "__main__":
    main()
