from sources import io
from sources import map_info
from sources import move
import click

def iterate(state):
    keep_on = True
    while(keep_on):
        state = make_move(state)
        for char in state["characters"]:
            if len(char[4]) == 0:
                keep_on = False
    return state

def make_move(state):
    for char in state["characters"]:
        if len(char[4]) > 0:
            state = move.move(state, char[0])
    return state

@click.command()
@click.option('--input_file', default="data/input.txt")
@click.option('--out', default="data/output.txt")
def run(input_file, out):
    state = io.read_all_input(input_file)
    if(map_info.is_map_valid(state)):
        state = iterate(state)
        formated_data = io.format_data(state)
        if(io.output_data(formated_data, out)):
            print "Success"

if __name__ == "__main__":
    run()
