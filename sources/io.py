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
            mountains.append([int(line.split('-')[1]), int(line.split('-')[2])])
    return mountains


def read_all_treasures(path):
    input_file = open(path,'r')
    treasures = []
    for line in input_file.read().split('\n'):
        if(line[0] == 'T'):
            treasures.append([int(line.split('-')[1]), int(line.split('-')[2]), int(line.split('-')[3])])
    return treasures


def read_all_characters(path):
    input_file = open(path,'r')
    characters = []
    for line in input_file.read().split('\n'):
        if(line[0] == 'A'):
            characters.append([line.split('-')[1].strip(), int(line.split('-')[2]), int(line.split('-')[3]), line.split('-')[4].strip(), line.split('-')[5].strip(), 0])
    return characters


def read_all_input(path):
    return {
        'map_size': read_size_map(path),
        'moutains': read_all_mountains(path),
        'treasures': read_all_treasures(path),
        'characters': read_all_characters(path)
    }

def format_data(raw_data):
    map_details = "C - {0} - {1}\n".format(raw_data["map_size"][0], raw_data["map_size"][1])
    moutains_details = ""
    treasures_details = ""
    characters_details = ""
    for moutain in raw_data["moutains"]:
        moutains_details = moutains_details + "M - {0} - {1}\n".format(moutain[0], moutain[1])
    for treasure in raw_data["treasures"]:
        treasures_details = treasures_details + "T - {0} - {1} - {2}\n".format(treasure[0], treasure[1], treasure[2])
    for char in raw_data["characters"]:
        characters_details = characters_details + "A - {0} - {1} - {2} - {3} - {4}\n".format(char[0], char[1], char[2], char[3], char[5])
    return map_details + moutains_details + treasures_details + characters_details


def output_data(raw_data, path):
    output_file = open(path,"w")
    output_file.write(raw_data)
    return 1
