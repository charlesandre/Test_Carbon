def info_case(data, x, y):
    if x > data["map_size"][0] or y > data["map_size"][1]:
        return 4
    for treasure in data["treasures"]:
        if treasure[0] == x and treasure[1] == y:
            return 1
    for moutain in data["moutains"]:
        if moutain == (x,y):
            return 2
    for char in data["characters"]:
        if char[1] == x and char[2] == y:
            return 3
    return 0


def is_map_valid(data):
    #Check if all elements are on the map
    errors = []
    [x_size, y_size] = data["map_size"]
    for moutain in data["moutains"]:
        if moutain[0] >= x_size or moutain[1] >= y_size:
            errors.append("Moutains out of bounds")
    for treasure in data["treasures"]:
        if treasure[0] >= x_size or treasure[1] >= y_size:
            errors.append("Treasures out of bounds")
    for char in data["characters"]:
        if char[1] >= x_size or char[2] >= y_size:
            errors.append("Character out of bounds")
        for char2 in data["characters"]:
            if char[0] != char2[0] and char[1] == char2[1] and char[2] == char2[2]:
                errors.append("Two characters are one the same spot")
    if len(errors) == 0:
        return True
    else:
        return [False, errors]
