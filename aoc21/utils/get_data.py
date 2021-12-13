import pathlib


def get_data(file_name, DEBUG=False) -> list:
    """
    Get the data from the data file.
    """
    if DEBUG:
        FILE_PATH = pathlib.Path("__file__").parent.parent / "test"

    else:
        FILE_PATH = pathlib.Path("__file__").parent.parent / "question"

    with open(FILE_PATH.joinpath(file_name + ".txt")) as f:
        lines = f.read().splitlines()

    return lines
