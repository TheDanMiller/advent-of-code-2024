from common.utils import read_file, find_relative_path


def find_diff(i: int, j:int) -> int:
    if i >= j:
        return i - j
    return j - i


def solve_part_one(use_sample: bool):
    print("Hello from solution")

    # Resolve path relative to this script's directory
    if use_sample:
        puzzle_input = find_relative_path('sample.txt', __file__)
    else:
        puzzle_input = find_relative_path('part1.txt', __file__)

    first_digit, second_digit, distance = [], [], 0
    # Read and process the file
    numbers = list(read_file(puzzle_input))
    for number_line in numbers:
        i, j = map(int, number_line.split())
        first_digit.append(i)
        second_digit.append(j)

    first_digit.sort()
    second_digit.sort()
    for i, j in zip(first_digit, second_digit):
        distance += find_diff(i, j)

    print(distance)


def solve_part_two(use_sample: bool):
    print("Hello from solution")

    # Resolve path relative to this script's directory
    if use_sample:
        puzzle_input = find_relative_path('sample.txt', __file__)
    else:
        puzzle_input = find_relative_path('input.txt', __file__)

    first_digit, second_digit, score = [], {}, 0
    # Read and process the file
    numbers = list(read_file(puzzle_input))
    for number_line in numbers:
        i, j = map(int, number_line.split())
        first_digit.append(i)
        if j in second_digit:
            second_digit[j] += 1
        else:
            second_digit[j] = 1

    for index, i in enumerate(first_digit):
        if i in second_digit:
            first_digit[index] = i * second_digit[i]
        else:
            first_digit[index] = 0
    print(sum(first_digit))