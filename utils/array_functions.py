"""Module for 2D array operations including padding and printing."""

from typing import List, TypeVar

T = TypeVar("T", int, str)


def _validate_array(array: List[List[T]], padding: int) -> int:
    """
    Validate the input array and padding parameters.

    Args:
        array: The 2D array to validate.
        padding: The padding value to validate.

    Returns:
        The length of the first row (number of columns).

    Raises:
        ValueError: If the array is empty, not rectangular, or padding is negative.
        TypeError: If the input is not a valid 2D array structure.
    """
    # Validate input array is not None
    if array is None:
        raise TypeError("Array cannot be None")

    # Validate array is not empty
    if not array or len(array) == 0:
        raise ValueError("Array cannot be empty")

    # Validate array is a list of lists
    if not isinstance(array, list) or not all(isinstance(row, list) for row in array):
        raise TypeError("Input must be a 2D array (list of lists)")

    # Validate array is not empty and rows are not empty
    if any(len(row) == 0 for row in array):
        raise ValueError("Array rows cannot be empty")

    # Validate array is rectangular (all rows have the same length)
    first_row_length = len(array[0])
    if not all(len(row) == first_row_length for row in array):
        raise ValueError(
            "Array must be rectangular (all rows must have the same length)"
        )

    # Validate padding is non-negative
    if padding < 0:
        raise ValueError("Padding must be non-negative")

    return first_row_length


def pad_2d_array(array: List[List[T]], padding: int, padding_char: T) -> List[List[T]]:
    """
    Pad a 2D array with a specified character on all sides.

    Args:
        array: The 2D array to pad (list of lists).
        padding: The number of rows/columns to add on each side.
        padding_char: The character/value to use for padding.

    Returns:
        A new 2D array with padding applied on all sides.

    Raises:
        ValueError: If the array is empty, not rectangular, or padding is negative.
        TypeError: If the input is not a valid 2D array structure.

    Example:
        >>> array = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        >>> padded = pad_2d_array(array, 2, 0)
        >>> # Returns:
        >>> # [[0,0,0,0,0,0,0],
        >>> #  [0,0,0,0,0,0,0],
        >>> #  [0,0,1,1,1,0,0],
        >>> #  [0,0,1,1,1,0,0],
        >>> #  [0,0,1,1,1,0,0],
        >>> #  [0,0,0,0,0,0,0],
        >>> #  [0,0,0,0,0,0,0]]
    """
    # Validate input and get dimensions
    first_row_length = _validate_array(array, padding)

    # Early return for zero padding
    if padding == 0:
        return [row[:] for row in array]

    # Calculate dimensions of the padded array
    original_rows = len(array)
    original_cols = first_row_length
    padded_rows = original_rows + 2 * padding
    padded_cols = original_cols + 2 * padding

    # Create the padded array filled with padding character
    padded_array: List[List[T]] = [
        [padding_char for _ in range(padded_cols)] for _ in range(padded_rows)
    ]

    # Copy original array into the center of the padded array
    for i, row in enumerate(array):
        for j, value in enumerate(row):
            padded_array[i + padding][j + padding] = value

    return padded_array


# create a function that transforms a 1d array to a 2d array based on a split character. each item in the 1d array will be a row in the 2d array, and each character in the item will be an element in the row.
def transform_1d_to_2d(array: List[str], split_char: str = "") -> List[List[str]]:
    """
    Transform a 1D array of strings into a 2D array based on a split character.

    Args:
        array: The 1D array of strings to transform.
        split_char: The character to split each string into elements.

    Returns:
        A 2D array where each row corresponds to an item in the 1D array,
        and each element in the row corresponds to a character in the item.

    Example:
        >>> array = ["abc", "def", "ghi"]
        >>> transformed = transform_1d_to_2d(array, "")
        >>> # Returns:
        >>> # [['a', 'b', 'c'],
        >>> #  ['d', 'e', 'f'],
        >>> #  ['g', 'h', 'i']]
    """
    return [
        list(item) if split_char == "" else item.split(split_char) for item in array
    ]


# create a function that splits elements in items in a 1d array based on a split character and returns a 1d array
def split_1d_array(array: List[str], split_char: str) -> List[str]:
    """
    Split elements in a 1D array based on a split character.

    Args:
        array: The 1D array of strings to split.
        split_char: The character to split each string into elements.
    Returns:
        A 1D array where each element is a part of the original strings split by the split character.
    """
    return [element for item in array for element in item.split(split_char)]


def print_2d_array(arr: List[List[int]]) -> None:
    """
    Print a 2D array in a formatted way.

    Args:
        arr: The 2D array to print.
    """
    for row in arr:
        print(" ".join(str(elem) for elem in row))
