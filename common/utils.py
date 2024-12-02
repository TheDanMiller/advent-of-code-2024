import os


def read_file(file_path: str) -> iter:
    # reads file and returns it as an iterable
    with open(file_path, 'r') as input_file:
        for line in input_file:
            yield line.strip()


def find_relative_path(file_name: str, current_file: str) -> str:
    current_dir = os.path.dirname(current_file)
    return os.path.join(current_dir, file_name)
