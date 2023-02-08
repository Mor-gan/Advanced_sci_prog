from test import double_list


def test_double_list():
    my_list = [1, 2, 3]
    doubled_list = double_list(my_list)

    assert doubled_list == [2, 4, 6]


def test_double_list_relative():
    my_list = [1, 2, 3]
    doubled_list = double_list(my_list)

    assert my_list[0] * 2 == doubled_list[0]