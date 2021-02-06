def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible \
    looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("45453*", 5)
    False
    """
    res = 1
    houses = input_line[1:-1]
    now = int(houses[0])

    for i in range(len(houses)):
        if int(houses[i]) > now:
            res += 1
            now = int(houses[i])

    if res == pivot:
        return True
    return False


print(left_to_right_check("412453*", 4))
