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
        if process_line(list(map(int, number_line.split())), False):
            good_lines += 1

    print(f"Good line count is: {good_lines}")


def validate_line(nums: list, is_increasing: bool, second_validation: bool) -> bool:
    if is_increasing:
        for i in range(1, len(nums)):
            delta = nums[i] - nums[i - 1]
            if delta < 1 or delta > 3:
                if second_validation:
                    return False
                else:
                    options = []
                    if len(nums) > 1:
                        options.append(process_line(nums[1:], True))  # Remove first element
                    if len(nums) > 1:
                        options.append(process_line(nums[:-1], True))  # Remove last element
                    if i + 1 < len(nums):
                        options.append(process_line(nums[:i] + nums[i + 1:], True))  # Remove current index

                    return any(options)
    else:
        for i in range(1, len(nums)):
            delta = nums[i] - nums[i - 1]
            if delta > -1 or delta < -3:
                if second_validation:
                    return False
                else:
                    options = []
                    if len(nums) > 1:
                        options.append(process_line(nums[1:], True))  # Remove first element
                    if len(nums) > 1:
                        options.append(process_line(nums[:-1], True))  # Remove last element
                    if i + 1 < len(nums):
                        options.append(process_line(nums[:i] + nums[i + 1:], True))  # Remove current index

                    return any(options)
    return True


def process_line(line: list, is_second_validation: bool) -> bool:
    is_increasing = True
    if line[1] < line[0]:
        is_increasing = False
    return validate_line(line, is_increasing, is_second_validation)