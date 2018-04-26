def info_case(data, x, y):
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