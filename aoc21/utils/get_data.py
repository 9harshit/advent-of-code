import pathlib


def get_data(DEBUG=False) -> list:
    """
    Get the data from the data file.
    """
    if DEBUG:
        FILE_PATH = pathlib.Path("__file__").parent.parent / "test"

    else:
        FILE_PATH = pathlib.Path("__file__").parent.parent / "question"

    with open(FILE_PATH.joinpath("aoc1.txt")) as f:
        lines = f.read().splitlines()

    return lines
