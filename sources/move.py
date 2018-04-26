import map_info

def move(raw_data, name):
    for char in raw_data["characters"]:
        if char[0] == name:
            new_char = char
    if new_char[4][0] != 'A':
        for char in raw_data["characters"]:
            if char[0] == name:
                char = modify_direction(new_char)
        return raw_data
    else:   
        x = 0
        y = 0
        if new_char[3] == 'S':
            x = 1
        if new_char[3] == 'N':
            x = -1
        if new_char[3] == 'E':
            y = +1
        if new_char[3] == 'O':
            y = -1
        new_case = map_info.info_case(raw_data, new_char[1]+1, new_char[2])
        print new_case
        if new_case == 0:
            new_char[1] += 1
        if new_case == 1:
            new_char[1] += 1
    return new_char




def modify_direction(char):
    move = char[4][0]
    curdir = char[3]
    if move == 'G':
        if curdir == 'E':
            newdir = 'N'
        if curdir == 'N':
            newdir = 'O'
        if curdir == 'O':
            newdir = 'S'
        if curdir == 'S':
            newdir = 'E'
    if move == 'D':
        if curdir == 'E':
            newdir = 'S'
        if curdir == 'S':
            newdir = 'O'
        if curdir == 'O':
            newdir = 'N'
        if curdir == 'N':
            newdir = 'E'
    new_char = char
    new_char[3] = newdir
    new_char[4] = char[4][1:]
    return new_char