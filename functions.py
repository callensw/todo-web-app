import os
import sys


def get_file_path(filename):
    if getattr(sys, 'frozen', False):
        # If running as an executable
        base_dir = os.path.dirname(sys.executable)
    else:
        # If running as a script
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, filename)


# Construct the absolute path to todos.txt
FILEPATH = get_file_path("todos.txt")


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
