import re
import itertools
import numpy
from pprint import pprint

def get_data():
    f = open("input.txt", "r")
    data = f.readlines()
    data1 = [re.sub('\n', '', line) for line in data]
    return data1

def get_test_data(number_of_lines):
    f = open("input.txt", "r")
    for line in range(number_of_lines):
        pass

def square_or_tree(given):
    if given == '.':
        return 'O'
    elif given == '#':
        return 'X'

def encountered(right, down, data):
    i = 0
    trees = []
    square = []
    stop = len(data) // down
    while i < stop:
        print([(i*down, i*right), square_or_tree(data[(i*down)][(i*right) % len(data[i])]), data[(i*down)][(i*right) % len(data[i])], ((i+1)*down, (i+1)*right), ((i*down), (i*right) % len(data[i])), (((i+1)*down), ((i+1)*right) % len(data[i]))])
        if square_or_tree(data[(i*down)][(i*right) % len(data[i])]) == 'O':
            square.append('O')
        else:
            trees.append('X')
        i += 1
    return {"squares": len(square), "trees": len(trees)}

def main():
    data = get_data()
    #print(data)
    #encountered(3, 1, data)
    #print(data[322])
    #print(data[1])
    #print(data[1][2])
    #result = encountered(3, 1, data)
    #print(data[1][3])
    #print(data[2][6])
    #print(len(result['trees']))
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    d = []
    for slope in slopes:
        d.append(encountered(slope[0], slope[1], data))
    print(d)
        
if __name__ == "__main__":
    main()