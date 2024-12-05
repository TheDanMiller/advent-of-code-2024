from common.utils import read_file, find_relative_path

def solve(use_sample: bool):

    # Resolve path relative to this script's directory
    if use_sample:
        puzzle_input = find_relative_path('sample.txt', __file__)
    else:
        puzzle_input = find_relative_path('input.txt', __file__)

    word_search_matrix = []
    for line in read_file(puzzle_input):
        word_search_matrix.append(list(line.strip()))
    print (word_search_matrix)