def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("input.txt")
    ['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***']
    """
    digits = []

    with open(path, 'r') as data:

        for line in data:
            line = line.strip()
            line = line.split(' ')
            str_digits = []

            for digit in line:
                str_digits.append(digit)

            digits.extend(str_digits)

    return digits


# print(read_input("input.txt"))


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    line_lst = [x for x in input_line]
    for i in range(len(input_line) - 1):
        if input_line[i] < input_line[i+1]:
            pivot -= 1

    if pivot == 1:
        return True
    return False


# print(left_to_right_check("452453*", 5))


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for small_lst in board:
        for element in small_lst:
            if element == '?':
                return False
    return True


# print(check_not_finished_board(
#     ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    element_united = []
    for small_lst in board:
        element_united = [s.replace('*', '') for s in small_lst]
        del element_united[0]
        del element_united[-1]

        while '' in element_united:
            element_united.remove('')

        len_start = len(element_united)
        len_end = len(set(element_united))

        if len_start > len_end:
            return False

    return True


# print(check_uniqueness_in_rows(
#     ['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***']))


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:
        line_splitted = [x for x in line]

        if line_splitted[0] != '*':
            result = left_to_right_check(line, int(line_splitted[0]))
            if result == False:
                return False

        elif line_splitted[-1] != '*':
            line_splitted.reverse()
            result = left_to_right_check(
                str(line_splitted), int(line_splitted[0]))
            if result == False:
                return False
    return True


print(check_horizontal_visibility(
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    all_lines = []
    for line in board:
        all_lines.append([x for x in line])

    column = []
    all_columns = []
    for i in range(len(all_lines)):
        for line in all_lines:
            column.append(line[i])
        all_columns.append(str(column))
        column = []

    if check_uniqueness_in_rows(all_columns) == False:
        return False
    elif check_horizontal_visibility(all_columns) == False:
        return False
    return True


print(check_columns(['***21**', '412553*', '423145*',
                     '*543215', '*35214*', '*41532*', '*2*1***']))


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    if check_not_finished_board(board) == False or check_uniqueness_in_rows(board) == False or check_horizontal_visibility == False or check_columns == False:
        return False
    return True


print(check_skyscrapers("check.txt"))

# if __name__ == "__main__":
#     print(check_skyscrapers("check.txt"))
