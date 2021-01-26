import pytest

test_list_data = [1,2,3,4,5]
def test_list_data_one():
    test_list_data.pop(0)
    assert len(test_list_data) == 4

test_list_cl = ["apple", "banana","orange"]
def test_clear():
    test_list_cl.clear()
    assert test_list_cl == []

test_list_ct = [1,4,5,6,7, 7,7]
def test_count():
    assert test_list_ct.count(7) == 3

test_list_in = ["Bmv", "Toyota", "Porshe", "Mersedes-benc", "Audi"]
def test_index():
    assert test_list_in.index("Audi") == 4

test_list_rev = [1,1,2,2,2,2,4,5,6,5,6]
test_list_two = [6,5,6,5,4,2,2,2,2,1,1]
def test_reverse():
    test_list_rev.reverse()
    assert test_list_rev == test_list_two

@pytest.mark.parametrize("list_input, expected", [("2 + 3", 5), ("20 + 20", 40), ("2 * 8", 16)])
def test_list_param(list_input, expected):
    assert eval(list_input) == expected


