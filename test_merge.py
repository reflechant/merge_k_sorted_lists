from merge_01 import merge


def test_zero_lines():
    assert list(merge([])) == []


def test_one_line_zero_elements():
    assert list(merge([[0]])) == []


def test_one_line_one_zero_element():
    assert list(merge([[1, 0]])) == [0]


def test_one_line_one_nonzero_element():
    assert list(merge([[1, 5]])) == [5]


def test_one_line_multiple_elements():
    assert list(merge([[3, 7, 8, 9]])) == [7, 8, 9]
    assert list(merge([[3, 0, 0, 0]])) == [0, 0, 0]


def test_multiple_lines_of_zero_element():
    assert list(merge([[0], [0]])) == []
    assert list(merge([[0], [0], [0]])) == []


def test_multiple_lines_of_one_element():
    assert list(merge([[1, 0], [1, 0]])) == [0, 0]
    assert list(merge([[1, 4], [1, 5]])) == [4, 5]
    assert list(merge([[1, 5], [1, 4]])) == [4, 5]


def test_generic_case():
    assert list(merge([[6, 2, 26, 64, 88, 96, 96],
                       [4, 8, 20, 65, 86],
                       [7, 1, 4, 16, 42, 58, 61, 69],
                       [1, 84]])) == [1, 2, 4, 8, 16, 20, 26, 42,
                                      58, 61, 64, 65, 69, 84, 86,
                                      88, 96, 96]
