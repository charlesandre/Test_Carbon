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
