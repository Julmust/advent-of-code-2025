def read_input_file(file_path: str) -> str:
    """Read the input file and return its contents as a list of strings."""
    # pylint: disable=W1514
    with open(file_path, "r") as file:
        return [row for row in file.read().splitlines() if row]
