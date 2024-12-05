from common.utils import read_file, find_relative_path
import re


def solve(use_sample: bool):

    # Resolve path relative to this script's directory
    if use_sample:
        puzzle_input = find_relative_path('sample.txt', __file__)
    else:
        puzzle_input = find_relative_path('input.txt', __file__)

    corrupted_memory = list(read_file(puzzle_input))  # Read file lines into a list
    corrupted_line = " ".join(corrupted_memory)
    regex = r"mul\((\d+),(\d+)\)"

    # Process each line
    all_matches = re.findall(regex, corrupted_line)

    # Print all matches found
    sum = 0
    for match in all_matches:
        delta = int(match[0]) * int(match[1])
        sum += delta

    print (f"The sum of the multiplied instructions is: {sum}")
    # Regex to find matching patterns mul(int, int)
    # multiple those ints and add to count
    # print the heck out of the count