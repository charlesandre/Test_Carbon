import numpy as np

def read_size_map(path):
    input_file = open(path,'r') 
    first_line = input_file.read().split('\n')[0]
    if(first_line[0] == 'C'):
        width = first_line.split('-')[1]
        height = first_line.split('-')[2]
        return [int(width), int(height)]
    else:
        return "Error with the input file, missing 'C' line"


def read_all_mountains(path):
    input_file = open(path,'r')
    mountains = []
    for line in input_file.read().split('\n'):
        if(line[0] == 'M'):
            mountains.append((int(line.split('-')[1]), int(line.split('-')[2])))
    return mountains


def read_all_treasures(path):
    input_file = open(path,'r')
    treasures = []
    for line in input_file.read().split('\n'):
        if(line[0] == 'T'):
            treasures.append((int(line.split('-')[1]), int(line.split('-')[2]), int(line.split('-')[3])))
    return treasures
    

def read_all_characters(path):
    input_file = open(path,'r')
    characters = []
    for line in input_file.read().split('\n'):
        if(line[0] == 'A'):
            characters.append([line.split('-')[1].strip(), int(line.split('-')[2]), int(line.split('-')[3]), line.split('-')[4].strip(), line.split('-')[5].strip()])
    return characters


def read_all_input(path):
    return {
        'map_size': read_size_map(path),
        'moutains': read_all_mountains(path),
        'treasures': read_all_treasures(path),
        'characters': read_all_characters(path)
    }