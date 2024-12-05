from common.utils import read_file, find_relative_path


def solve(use_sample: bool):
    print("Hello from solution")

    # Resolve path relative to this script's directory
    if use_sample:
        puzzle_input = find_relative_path('sample.txt', __file__)
    else:
        puzzle_input = find_relative_path('input.txt', __file__)

    good_lines = 0
    numbers = list(read_file(puzzle_input))
    for number_line in numbers:
        if process_line(number_line):
            good_lines += 1

    print(f"Good line count is: {good_lines}")


def validate_line(nums: list, is_increasing: bool, second_validation: bool) -> bool:
    if is_increasing:
        for i in range(1, len(nums)):
            delta = nums[i] - nums[i - 1]
            if delta < 1 or delta > 3:
                return False
    else:
        for i in range(1, len(nums)):
            delta = nums[i] - nums[i - 1]
            if delta > -1 or delta < -3:
                return False
    return True


def process_line(line: str) -> bool:
    nums = list(map(int, line.split()))
    is_increasing = True
    if nums[1] < nums[0]:
        is_increasing = False
    return validate_line(nums, is_increasing, False)