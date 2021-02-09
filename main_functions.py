import json
import sys

def path_to_aray(path):
    data_array= []
    cleanPath = path.rstrip("\n")
    with open(cleanPath) as x:
        for line in x:
            line = line.rstrip("\n")
            data_array.append(line)
        return data_array

def clear_that_file(file):
    open('config.txt', 'w').close() #best method to erase a text file apprently
