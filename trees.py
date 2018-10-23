import copy
import fileinput
import time
import pprint as pp

def main():
    file_input = fileinput.input()

    tree = {'relation':[], 'attributes':[], 'data':[]}

    for line in file_input:
        if(line[0] != '%' and line != '\n'):
            if(line[0:9] == '@relation'):
                tree['relation'].append(line[10:])
            elif(line[0:10] == '@attribute'):
                tree['attributes'].append(line[11:])
            elif(line[0:5] != '@data'):
                tree['data'].append(line)

    pp.pprint(tree)

if __name__ == "__main__":
    main()
