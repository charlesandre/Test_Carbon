import map_info

def move(raw_data, name):
    for char in raw_data["characters"]:
        if char[0] == name:
            new_char = char
            if new_char[4][0] != 'A':
                new_char = modify_direction(new_char)
            else:
                x = 0
                y = 0
                if new_char[3] == 'S':
                    y = 1
                if new_char[3] == 'N':
                    y = -1
                if new_char[3] == 'E':
                    x = 1
                if new_char[3] == 'O':
                    x = -1
                new_case = map_info.info_case(raw_data, new_char[1]+x, new_char[2]+y)
                if new_case == 0 or new_case == 1:
                    new_char[1] = int(new_char[1]) + x
                    new_char[2] = int(new_char[2]) + y
                if new_case == 1:
                    new_char = add_one_point(new_char)
                    raw_data = remove_one_treasure(raw_data, new_char[1], new_char[2])
            for char in raw_data["characters"]:
                if char[0] == name:
                    char = remove_last_move(new_char)
                    return raw_data



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
    return new_char


def remove_last_move(char):
    char[4] = char[4][1:]
    return char

def remove_one_treasure(raw_data, x, y):
    for treasure in raw_data["treasures"]:
        if treasure[0] == x and treasure[1] == y and treasure[2]>0:
            treasure[2] = treasure[2] -1
            return raw_data
    return False

def add_one_point(char):
    char[5] = int(char[5]) +1
    return char
