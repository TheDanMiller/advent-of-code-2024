from common.utils import read_file, find_relative_path
import re


def remove_invalid_instructions(corrupted_line: str) -> str:
    do_instructions = []
    searching_index = 0
    dont_search_string = "don't()"
    do_search_string = "do()"

    while True:
        dont_index = corrupted_line.find(dont_search_string, searching_index)

        #find dont
        if dont_index == -1:
            do_instructions.append(corrupted_line[searching_index:])
            break
        do_instructions.append(corrupted_line[searching_index: dont_index])
        searching_index = dont_index + len(dont_search_string)

        # find do, should not find don't because of inclusion of () in search string
        do_index = corrupted_line.find(do_search_string, searching_index)
        if do_index == -1:
            break
        searching_index = do_index + len(do_search_string)

    return " ".join(do_instructions)


def solve(use_sample: bool):

    # Resolve path relative to this script's directory
    if use_sample:
        puzzle_input = find_relative_path('sample.txt', __file__)
    else:
        puzzle_input = find_relative_path('input.txt', __file__)

    corrupted_memory = list(read_file(puzzle_input))  # Read file lines into a list
    corrupted_line = " ".join(corrupted_memory)
    # pull out the don't sections
    shorter_corrupted_string = remove_invalid_instructions(corrupted_line)
    regex = r"mul\((\d+),(\d+)\)"

    # Process each line
    all_matches = re.findall(regex, shorter_corrupted_string)

    # Print all matches found
    sum = 0
    for match in all_matches:
        delta = int(match[0]) * int(match[1])
        sum += delta

    print (f"The sum of the multiplied instructions is: {sum}")