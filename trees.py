import copy
import fileinput
import time
import pprint as pp

def main():
    file_input = fileinput.input()

    tree = {'relation':[], 'attributes':[], 'data':[]}

    for line in file_input:
        if(line[0:8] == '@relation'):
            tree['relation'].append(line)
        elif(line[0:9] == '@attribute'):
            tree['attributes'].append(line)
        elif(len(line) > 0 && line[0:5] != '@data'):
            tree['data'].append(line)

    print(tree)

if __name__ == "__main__":
    main()
