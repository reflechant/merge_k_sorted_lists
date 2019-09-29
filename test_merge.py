from merge_01 import merge


def test_zero_lines():
    assert (merge(0, lines)) == []


def test_one_line_zero_elements():
    assert (merge(1, lines)) == []


def test_one_line_one_zero_element():
    assert (merge(1, lines)) == [0]


def test_one_line_one_nonzero_element():
    assert (merge(1, lines)) == [5]
