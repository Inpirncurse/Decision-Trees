import copy
import fileinput
import time
import pprint as pp
import random

def add_attribute(string, attributes):
    string = string.split(' ')
    name = string[0].replace(' ','')
    attributes[name] = []
    for element in string[1:]:
        attributes[name].append(element.replace(',','').replace(' ','').replace('}','').replace('{',''))

def entropy(data):
    value = random.uniform(0.0, 1.0)
    print(value)
    return value

def main():
    file_input = fileinput.input()
    tree = {}
    attributes = {}

    tree[0] = {'data':[]}
    for line in file_input:
        if(line[0] != '%' and line != '\n'):
            if(line[0:10] == '@attribute' or line[0:10] == '@ATTRIBUTE'):
                add_attribute(line[11:].replace('\n',''), attributes)
            elif(line[0:5] != '@data' and line[0:5] != '@DATA' and line[0:9] != '@relation' and line[0:9] != '@REALTION'):
                tree[0]['data'].append(line.replace('\n','').split(','))
    tree[0]['parent'] = 'NULL'


    pp.pprint(tree)
    pp.pprint(attributes)

if __name__ == "__main__":
    main()
