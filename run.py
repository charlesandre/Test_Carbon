from sources import io
from sources import map_info
from sources import move
import click

def run(in_file, out_file):
    state = io.read_all_input(in_file)
    if(map_info.is_map_valid(state)):
        state = iterate(state)
        formated_data = io.format_data(state)
        if(io.output_data(formated_data, out_file)):
            print "Success"
            return True
    return False



def iterate(state):
    keep_on = True
    while(keep_on):
        keep_on = False
        state = make_move(state)
        for char in state["characters"]:
            if len(char[4]) > 0:
                keep_on = True
    return state

def make_move(state):
    for char in state["characters"]:
        if len(char[4]) > 0:
            state = move.move(state, char[0])
    return state

@click.command()
@click.option('--in_file', default="input.txt")
@click.option('--out_file', default="output.txt")
def start(in_file, out_file):
    in_file = "data/" + in_file
    out_file = "data/" + out_file
    run(in_file, out_file)

if __name__ == "__main__":
    start()
